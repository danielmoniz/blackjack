#!/usr/bin/env python

from player import Player
from dealer import Dealer
from deck import Deck
from game import Game

# Run the actual game loop, turn by turn.


# generate initial players, dealer, and deck
# initialize game board: deal hands, and anything else that needs to be done

# GAME LOOP - retrieve player input until they have lost the round or are
# standing (I think)

# while game is not over:
    # for each player at the table:
        # get player input and act on that action
    # dealer performs action (reveals card, I think?)

    # check state of game. Is everybody standing or surrendered?
    # (do this by asking each player for input, and having them all be
    # unable to do so.)
        # if everybody is finished, 
            # enter dealer action loop until round is complete
            # Turn complete. Move chips, clear cards, adjust the turn counter,
            # allow first-turn actions. (etc!)
        # ELSE, ie. somebody is not finished:
            # disallow some first-turn actions.
            # continue to the start of the Game Loop.
        
    
    # retrieve input from players if necessary

    # set game state (eg. set 'over' if it's over to kill the game loop)
""" TESTING AREA """
deck = Deck()
deck.shuffle()
# For now, create a single player. Should allow for more.
players = [Player()]
dealer = Dealer

# Initialize game object
game = Game(deck, players)

deck = game.deck
players = game.players
print players
print players[0]

"""while deck.get_num_cards() > 0:
    print deck.get_next_card()"""
