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
        """Deal new hands, and perform any other start-of-turn actions."""
        self.deal_initial_hands()
        # @TODO Ask for bets from each player.
        for player in self.players:
            pass
            player.place_bet(self.min_bet)


    def end_turn(self):
        """Perform any tasks required at the end of a turn. Eg. empty hands and
        move chips around."""
        # Allow first-turn actions
        # Set players' turns to not be over.
        for player in self.players:
            player.set_turn_over(False)
        # End the game if there are no more players.
        if len(self.players) == 0:
            self.game_over = True

        return False

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
            new_hand = []
            for i in range(num_cards):
                new_hand.append(self.deck.get_next_card())
            player.assign_hand(new_hand)
            """print "Newly assigned cards:"
            for card in new_hand:
                print card"""

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
                if player.get_hand_value(hand) > 21:
                    # @TODO Move bets
                    print "folded hand. value", player.get_hand_value(hand)
                    player.fold_hand(hand)
                    player.set_turn_over()
