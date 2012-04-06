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
    # determine state of game

    # retrieve input from players if necessary

    # set game state (eg. set 'over' if it's over to kill the game loop)
""" TESTING AREA """
deck = Deck()
deck.shuffle()
# For now, create a single player. Should allow for more.
players = [Player()]

game = Game(deck, players)

deck = game.deck
players = game.players
print players
print players[0]

"""while deck.get_num_cards() > 0:
    print deck.get_next_card()"""
