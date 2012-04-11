from user_interface import UserInterface
from hand import Hand

UI = UserInterface()

class Game:
    def __init__(self, deck, dealer = None, players = None):
        """Set up game object. Define min/max bets, whether the game is over or
        not, the deck, players, and dealer, and the maximum number of
        players."""
        self.min_bet = 10
        self.max_bet = 100
        self.over = False
        self.deck = deck
        self.max_players = 2
        self.dealer = dealer

        if players == None:
            self.players = []
        else:
            self.players = players

    def end_game(self):
        """Simply set the game state to be over."""
        self.over = True

    def start_turn(self):
        """Deal new hands, and take initial user bets (minimum). Perform any
        other start-of-turn actions.  Boot players if they do not have enough
        chips for a minimum bet. End the game if there are no more players."""
        UI.start_turn()

        # Set players and dealer to a new turn.
        for player in self.players:
            player.set_new_turn()
        self.dealer.set_new_turn()

        self.deal_initial_hands()
        # Ask for bets from each player.

        # Kick players who cannot afford the minimum bet
        for player in self.players[:]:
            if not player.has_enough_chips(self.min_bet):
                self.kick_player(player)

        # @TODO Allow user to select a bet other than the minimum.
        for player in self.players:
            message = "Select a bet size (no input is {}):".format(self.min_bet)
            bet_size = player.get_user_integer_input(message, self.min_bet, self.min_bet, self.max_bet)
            player.place_bet(bet_size)

        # End the game if there are no more players.
        if len(self.players) == 0:
            self.end_game()

    def end_turn(self):
        """Perform any tasks required at the end of a turn. Eg. empty hands and
        compare dealer score to move chips around accordingly."""
        # Evaluate hands, compare to dealer's, and move chips accordingly.
        self.move_chips()

        # Clear player hands and dealer's hand. Iterate through each player's
        # hands and the dealer's hand to discard them individually
        hands_to_discard = []
        for player in self.players:
            hands = player.purge_hands()
            for hand in hands:
                hands_to_discard.append(hand)
        dealer_hand = self.dealer.get_hand()
        self.dealer.purge_hands()
        hands_to_discard.append(dealer_hand)

        self.discard_hands(hands_to_discard)

    def evaluate_hands(self, player_hand, dealer_hand):
        """Evaluates two valid (ie <= 21) hands from the point of view of the
        first. Returns a number of different outcomes depending on the hands:
        'win', 'lose', 'push'. A 'push' occurs when two hands are tied and neither or both of
        them are blackjacks. (If the two are tied and one is a blackjack while
        the other isn't, it is a win or a loss.)"""

        # If a player folds, they lose because the dealer did not yet have a
        # chance to fold.
        if player_hand.folded:
            return 'lose'
        # If the dealer folded but not the player, then the player wins.
        elif dealer_hand.folded:
            UI.player_hand_fold(self.dealer, dealer_hand, dealer_hand.best_value())
            return 'win'
        player_val, dealer_val = player_hand.best_value(), dealer_hand.best_value()

        # Win or lose if the hand values are not equal -------
        if player_val > dealer_val:
            return 'win'
        elif player_val < dealer_val:
            return 'lose'
        else: # in the case of a tie
            if player_hand.is_blackjack() == dealer_hand.is_blackjack():
                return 'push'
            else:
                # At this point, player_hand having blackjack implies dealer_hand does not
                if player_hand.is_blackjack():
                    return 'win'
                else:
                    return 'lose'

    def move_chips(self):
        """Calculates outcomes of hands and move chips accordingly.
        Also prints off information about the results.
        @TODO Printed data should be in a separate UI class!"""
        dealer_hand = self.dealer.get_hand()
        dealer_score = dealer_hand.best_value()
        UI.player_score(self.dealer, dealer_score)
        for player in self.players:
            for hand in player.hands:
                outcome = self.evaluate_hands(hand, dealer_hand)
                UI.player_hand_bet(player, hand)
                value, owner = hand.bet[0], hand.bet[1]

                UI.player_score(player, hand.best_value())

                # Move chips depending on the outcome.
                if outcome == 'win':
                    owner.add_chips(2 * value)
                    self.dealer.remove_chips(value)
                    UI.win_hand(owner, value)
                elif outcome == 'push':
                    # Replace chips
                    owner.add_chips(value)
                    UI.push_hand(owner, value)
                elif outcome == 'lose':
                    UI.lose_hand(owner, value)
                    self.dealer.add_chips(value)

    # @TODO This function DEFINITELY needs breaking up/refactoring.
    def accomodate_player_action(self, player, action, hand):
        """This function takes a player and an action as arguments and ensures that their action is performed.
        This is from the point of view of the game table itself. The player
        elects to make an action, and they carry out part of the required
        tasks. The game itself then provides them with new cards (or what have
        you) should they need them. Since every action takes place on a
        specific hand, a hand argument is required.
        Returns False if the action is bad, True if everything works."""
        # Delegate any personal functionality (eg. ending one's turn) to the
        # player class.
        player.perform_action(action)

        # Depending on the action provided, perform different effects.
        if action == 'hit':
            # Deal a single card to the player.
            new_card = self.deck.get_next_card()
            player.assign_new_card(new_card, hand)
            UI.deal_card(player, new_card)
        elif action == 'stand':
            # Do nothing; the player has ended their turn.
            pass
        elif action == 'split':
            # Split their hand in two if it matches a set of criteria.
            if hand.num_cards() == 2:
                card1, card2 = hand.cards
                if card1.get_value() == card2.get_value():
                    hand.prepare_split()
            else:
                # If they try to split when it is not possible, hit instead.
                # @TODO This is silly; they should simply be told they cannot
                # split and re-prompted.
                self.accomodate_player_action(player, 'hit', hand)
                return False
            pass
        elif action == 'double':
            # Double a player's bet and give them one more card.
            print hand
            print hand.bet
            # @TODO Check to see if hand.bet is None first. Fixes a bug that
            # occurs when doubling down with not enough chips available.
            if hand.bet == None or not player.has_enough_chips(hand.get_bet_value()):
                UI.double_down_fail(player)
                self.accomodate_player_action(player, 'hit', hand)
                return False

            # Return chips to owner, but double bet on the hand
            bet_value, owner = hand.bet
            owner.add_chips(bet_value)
            hand.clear_bet()
            owner.place_bet(2 * bet_value, hand)

            # Add a single card to the hand.
            player.assign_new_card(self.deck.get_next_card(), hand)
        elif action == "surrender":
            # Restore 50% (rounded down) of a bet's chips to its owner.
            bet_value, owner = hand.bet
            restore_value = bet_value / 2
            self.dealer.add_chips(bet_value - restore_value)
            owner.add_chips(restore_value)

            # Fold the hand so that it is cleaned up later.
            hand.fold()
        else:
            return False

        hand.validate()
        # if no hands remaining, end player's turn.
        valid_hands = [hand for hand in player.hands if not hand.folded]
        if len(valid_hands) == 0:
            player.set_turn_over()

        return True

    def add_player(self, player):
        """Add a new player to the table. Returns True if a player is added,
        and False otherwise."""
        if len(self.players) + 1 > self.max_players:
            UI.too_many_players(self.max_players)
            return False
        else:
            self.players.append(player)
            return True

    # @NOTE This is currently not used!
    def kick_player(self, player):
        """Remove a player from the game for losing.
        Returns True if they were successfully kicked, and false otherwise."""
        try:
            UI.lose(player)
            self.players.remove(player)
            return True
        except KeyError:
            return False
        
    def deal_initial_hands(self):
        """Deals hands for all players in the game.  Deal two cards to each bet
        box starting from the dealer's left, followed by one for the dealer.
        Note that this is NOT hole card play, where another card is dealt face
        down so that the game can end immediately if the dealer has a
        blackjack."""
        num_cards = 2
        for player in self.players:
            new_hand = Hand()
            for i in range(num_cards):
                new_card = self.deck.get_next_card()
                new_hand.add_card(new_card)
            player.assign_hand(new_hand)
            UI.deal_hand(player, new_hand)

        dealer_hand = Hand([self.deck.get_next_card()])
        self.dealer.assign_hand(dealer_hand)

    def validate_player_hands(self):
        """Iterate through players in the game, checking their hands. If any
        are invalid (over 21), remove them and move chips accordingly."""
        for player in self.players:
            for hand in player.hands:
                if hand.smallest_value() > 21:
                    UI.player_hand_fold(player, hand, hand.smallest_value())
                    player.fold_hand(hand)
            # if no hands remaining, end player's turn.
            valid_hands = [hand for hand in player.hands if not hand.folded]
            if len(valid_hands) == 0:
                player.set_turn_over()

    def split_player_hands(self):
        """Iterate through players and split any hands indicating that they
        need to be split.
        NOTE: Assumes that hand already fits the criteria for splitting."""
        for player in self.players:
            hands_copy = player.hands[:]
            for hand in hands_copy:
                if not hand.split:
                    return False

                card1, card2 = hand.cards
                bet_value, owner = hand.bet

                # Check if player can afford to split! If not,
                # un-split the hand and move on.
                if not player.has_enough_chips(bet_value):
                    hand.unsplit()
                    return False

                # Return bet value to owner
                owner.add_chips(bet_value)

                # Delete the old hand and make two new ones
                player.purge_hand(hand)
                new_card1 = self.deck.get_next_card()
                new_hand1 = Hand([card1, new_card1])
                
                new_card2 = self.deck.get_next_card()
                new_hand2 = Hand([card2, new_card2])

                player.assign_hand(new_hand1)
                player.assign_hand(new_hand2)
                owner.place_bet(bet_value, new_hand1)
                owner.place_bet(bet_value, new_hand2)

    def discard_hands(self, hands):
        """Communicates with the game's discard pile to discard hands."""
        for hand in hands:
            card_list = hand.cards
            for card in card_list:
                self.deck.discard(card)

"""
Deprecated: The dealer's hand is now validated every time he/she hits.
    def validate_dealer_hand(self):
        #Ensure the dealer's hand is not over 21, and that his hand is folded
        if he goes over.
        hand = self.dealer.get_hand()
        if hand.smallest_value > 21:
            self.dealer.fold_hand(hand)
            self.dealer.set_turn_over()
"""
