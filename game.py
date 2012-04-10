from hand import Hand

class Game:
    def __init__(self, deck = None, dealer = None, players = []):
        """Set up game object. Define min/max bets, whether the game is over or
        not, the deck, players, and dealer, and the maximum number of
        players."""
        self.min_bet = 10
        self.max_bet = 100
        self.over = False
        self.deck = deck
        self.max_players = 2
        self.dealer = dealer
        self.players = players

    def end_game(self):
        """Simply set the game state to be over."""
        self.over = True

    def start_turn(self):
        """Deal new hands, and take initial user bets (minimum). Perform any
        other start-of-turn actions.  Boot players if they do not have enough
        chips for a minimum bet. End the game if there are no more players."""
        # Set players and dealer to a new turn.
        for player in self.players:
            player.set_turn_over(False)
        self.dealer.set_turn_over(False)

        self.deal_initial_hands()
        # Ask for bets from each player.
        # @TODO Allow user to select a bet other than the minimum.
        self.players = [p for p in self.players if p.has_enough_chips]
        for player in self.players:
            player.place_bet(self.min_bet)

        # End the game if there are no more players.
        if len(self.players) == 0:
            self.end_game()

    def end_turn(self):
        """Perform any tasks required at the end of a turn. Eg. empty hands and
        compare dealer score to move chips around accordingly."""
        # Evaluate hands, compare to dealer's, and move chips accordingly.
        self.move_chips()

        # @TODO Allow first-turn actions
        # Clear player hands and dealer's hand
        for player in self.players:
            player.purge_hands()
        self.dealer.purge_hands()

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
            print dealer_hand, dealer_hand.folded
            print "dealer folded!"
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
        print "Dealer score:", dealer_score
        for player in self.players:
            for hand in player.hands:
                outcome = self.evaluate_hands(hand, dealer_hand)
                value, owner = hand.bet[0], hand.bet[1]
                print player, "score:", hand.best_value()
                # Move chips depending on the outcome.
                if outcome == 'win':
                    owner.add_chips(2 * value)
                    self.dealer.remove_chips(value)
                    print str(owner), "won", value, "chips!"
                elif outcome == 'push':
                    # Replace chips
                    owner.add_chips(value)
                    print str(owner), "broke even with", value, "chips."
                elif outcome == 'lose':
                    print str(owner), "lost", value, "chips."
                    self.dealer.add_chips(value)

    # @TODO This function probably needs breaking up/refactoring.
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
            print "Dealt:", new_card
        elif action == 'stand':
            # Do nothing; the player has ended their turn.
            pass
        elif action == 'split':
            # Split their hand in two if it matches a set of criteria.
            # @TODO
            if hand.num_cards() == 2:
                card1, card2 = hand.cards
                if card1.get_value() == card2.get_value():
                    hand.prepare_split()
            else:
                return False
            pass
        elif action == 'double down':
            # Double a player's bet and give them one more card.
            # @TODO
            pass
        else:
            return False

        # @TODO This needs to act on a per-hand basis, not on the whole player!
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
            print "Cannot have more than {} players!".format(self.max_players)
            return False
        else:
            self.players.append(player)
            return True

    # @NOTE This is currently not used!
    def kick_player(self, player):
        """Remove a player from the game for losing.
        Returns True if they were successfully kicked, and false otherwise."""
        try:
            print player, "loses!"
            # @TODO Move this message to the UI module.
            game.players.remove(player)
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
            print "Newly dealt cards:"
            print new_hand
            print "----------------"
            player.assign_hand(new_hand)
            #player.place_bet(self.min_bet, new_hand)

        dealer_hand = Hand([self.deck.get_next_card()])
        self.dealer.assign_hand(dealer_hand)

    def validate_player_hands(self):
        """Iterate through players in the game, checking their hands. If any
        are invalid (over 21), remove them and move chips accordingly."""
        for player in self.players:
            for hand in player.hands:
                if hand.smallest_value() > 21:
                    print "folded hand. value", hand.smallest_value()
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
                if hand.split:
                    print hand
                    card1, card2 = hand.cards

                    # Delete the old hand and make two new ones
                    player.purge_hand(hand)
                    new_card1 = self.deck.get_next_card()
                    new_hand1 = Hand([card1, new_card1])
                    
                    new_card2 = self.deck.get_next_card()
                    new_hand2 = Hand([card2, new_card2])

                    player.assign_hand(new_hand1)
                    player.assign_hand(new_hand2)

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
