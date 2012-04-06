class Game:
    def __init__(self, deck = None, players = []):
        self.max_bet = 100
        self.game_over = False
        self.deck = deck
        self.max_players = 2
        self.players = players

    def end_game(self):
        """Simply set the game state to be over."""
        self.game_over = True

    def end_turn_clean_up(self):
        """Perform any tasks required at the end of a turn. Eg. empty hands and
        move chips around."""
        pass

    # @TODO Is this necessary? Note that perform_action() is a player function.
    def act_on_action(self, player, action):
        """Receive an action from a player and make it happen."""
        return 

    def add_player(self, player):
        """Add a new player to the table. Returns True if a player is added,
        and False otherwise."""
        if len(self.players) >= self.max_players:
            print "Cannot have more than {} players!".format(self.max_players)
            return False
        else:
            self.players.append(player)
            return True
