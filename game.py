#!/usr/bin/env python

from player import Player
from dealer import Dealer
from deck import Deck

class Game:
    def __init__(self):
        self.max_bet = 100
        self.game_over = False

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

# Run the actual game loop, turn by turn.


# generate initial players, dealer, and deck
# initialize game board: deal hands, and anything else that needs to be done

# GAME LOOP - retrieve player input until they have lost the round or are
# standing (I think)

# while game is not over:
    # determine state of game

    # retrieve input from players if necessary

    # set game state (eg. set 'over' if it's over to kill the game loop)
