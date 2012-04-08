class Game:
    def __init__(self, deck = None, dealer = None, players = []):
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
        pass

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
            game.players.remove(player)
            # @TODO Print some message about a player losing.
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
            for card in new_hand:
                print card

    def deal_cards(self):
        """Deal a single card to each position that has a bet, clockwise from
        dealer's left, followed by a single card to the dealer. Then deal an initial card to each position in play."""
        pass

