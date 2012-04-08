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
            # allow first-turn actions, set players to have their turns not be
            # over. (etc!)
            # if there are no more players, or they have no chips:
                # Set the game to be over
            
        # ELSE, ie. somebody is not finished:
            # disallow some first-turn actions.
            # continue to the start of the Game Loop.
        
""" TESTING AREA """
deck = Deck()
deck.shuffle()
# For now, create a single player. Should allow for more.
players = [Player("Human 1")]
dealer = Dealer("Dealer")

# Initialize game object
game = Game(deck, dealer, players)
game.start_turn()

# GAME LOOP - retrieve player input until they have lost the round or are
while not game.over:
    # For each player at table, get actions, followed by dealer's action
    for player in players:
        action = player.get_action()
        player.perform_action(action)
        game.accomodate_player_action(player, action)
        for card in player.hands[0]:
            print card
    dealer_action = dealer.get_action()
    dealer.perform_action(dealer_action)

    # Check game state. Is everybody standing or surrendered?
    players_finished = True
    for player in players:
        if not player.turn_over:
            players_finished = False
            break

    if players_finished:
        # Enter dealer loop until dealer is finished
        while not dealer.turn_over:
            action = dealer.get_action()
            dealer.perform_action(action)

        # Turn is now over. Clean up the table and prepare for a new turn.
        game.end_turn()
        game.start_turn()
    else:
        # disallow first-turn actions. Move to start of loop
        continue



deck = game.deck
players = game.players
print players
print players[0]

"""while deck.get_num_cards() > 0:
    print deck.get_next_card()"""
