from hand import Hand

class Game:
    def __init__(self, deck = None, dealer = None, players = []):
        self.min_bet = 10
        self.max_bet = 100
        self.over = False
        self.deck = deck
        self.max_players = 2
        self.dealer = dealer
        self.players = players

    def end_game(self):
        """Simply set the game state to be over."""
        self.game_over = True

    def start_turn(self):
        """Deal new hands, and take initial user bets (minimum). Perform any
        other start-of-turn actions."""
        self.deal_initial_hands()
        # Ask for bets from each player.
        # @TODO Allow user to select a bet other than the minimum.
        for player in self.players:
            player.place_bet(self.min_bet)


    def end_turn(self):
        """Perform any tasks required at the end of a turn. Eg. empty hands and
        compare dealer score to move chips around accordingly."""
        # Evaluate hands and move chips accordingly.
        dealer_hand = self.dealer.get_hand()
        dealer_score = self.dealer.get_hand().best_value()
        print "Dealer score:", dealer_score
        for player in self.players:
            for hand in player.hands:
                outcome = self.evaluate_hands(hand, dealer_hand)
                value, owner = hand.bet[0], hand.bet[1]
                print player, "score:", hand.best_value()
                print owner
                if outcome == 'win':
                    owner.add_chips(2 * value)
                    print str(owner), "won", value, "chips!"
                elif outcome == 'push':
                    # Replace chips
                    owner.add_chips(value)
                    print str(owner), "broke even with", value, "chips."
                elif outcome == 'lose':
                    print str(owner), "lost", value, "chips."

                    
        # @TODO Allow first-turn actions
        # Clear player hands and set players' turns to not be over.
        for player in self.players:
            player.purge_hands()
            player.set_turn_over(False)

        # clear dealer's hand
        self.dealer.purge_hands()
        self.dealer.set_turn_over(False)

        # End the game if there are no more players.
        if len(self.players) == 0:
            self.game_over = True

        return False

    def evaluate_hands(self, hand1, hand2):
        """Evaluates two valid (ie <= 21) hands from the point of view of the
        first. Returns a number of different outcomes depending on the hands:
        'win', 'lose', 'push'. A 'push' occurs when two hands are tied and neither or both of
        them are blackjacks. (If the two are tied and one is a blackjack while
        the other isn't, it is a win or a loss.)"""
        #hand1_val, hand2_val = hand1.best_value(), hand2.best_value()
        if hand1.folded:
            return 'lose'
        elif hand2.folded:
            print hand2, hand2.folded
            print "dealer folded!"
            return 'win'
        hand1_val = hand1.best_value()
        hand2_val = hand2.best_value()
        # Win or lose if the hand values are not equal -------
        if hand1_val > hand2_val:
            return 'win'
        elif hand1_val < hand2_val:
            return 'lose'
        else: # in the case of a tie
            if hand1.is_blackjack() == hand2.is_blackjack():
                return 'push'
            else:
                # At this point, hand1 having blackjack implies hand2 does not
                if hand1.is_blackjack():
                    return 'win'
                else:
                    return 'lose'

    def accomodate_player_action(self, player, action):
        """This function takes a player and an action as arguments and ensures that their action is performed.
        This is from the point of view of the game table itself. The player elects to make an action, and they carry out part of the required tasks. The game itself then provides them with new cards (or what have you) should they need them."""
        if action == 'hit':
            new_card = self.deck.get_next_card()
            player.assign_new_card(new_card)
            print "Dealt:", new_card
        elif action == 'split':
            # @TODO
            pass
        elif action == 'double down':
            # @TODO
            pass
        else:
            return False

        return True

    def add_player(self, player):
        """Add a new player to the table. Returns True if a player is added,
        and False otherwise."""
        if len(self.players) >= self.max_players:
            print "Cannot have more than {} players!".format(self.max_players)
            return False
        else:
            self.players.append(player)
            return True

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
        box starting from the dealer's left, followed by one for the dealer and
        one face down."""
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
        print "is dealer's hand folded at start?", self.dealer.get_hand().folded

    # @TODO What is this function for if users are able to receive cards by
    # hitting?
    def deal_cards(self):
        """Deal a single card to each position that has a bet, clockwise from
        dealer's left, followed by a single card to the dealer."""
        pass

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

    def validate_dealer_hand(self):
        """Ensure the dealer's hand is not over 21, and that his hand is folded if he goes over."""
        hand = self.dealer.get_hand()
        if hand.smallest_value > 21:
            self.dealer.fold_hand(hand)
            self.dealer.set_turn_over()
