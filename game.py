class Game:
    def __init__(self):
        self.max_bet = 100
        self.game_over = False
        self.deck = None

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

