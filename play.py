#!/usr/bin/env python

from player import Player
from dealer import Dealer
from deck import Deck
from game import Game
from user_interface import UserInterface

# It is import that an imported player imported as 'Player' if you're using
# only the one player.
from ai_players import SplitDoublePlayer, HitPlayer, RandomPlayer

"""This file exists to start the game and help the Game class to direct the flow. 
It initializes the game object and runs the primary game loop. The primary game loop, in short, does the following:
1. receive input actions from each player.
2. Let the dealer have an action.
3. If everybody is done, the dealer does actions until he/she is finished.
4. End the turn and start a new one."""

UI = UserInterface()

UI.game_instructions()

# generate initial players, dealer, and deck
deck = Deck()
deck.shuffle()
# The discard pile is a deck of size 0

# For now, create a single player. Should allow for more.
# @TODO Ask for number of players and their names.
players = [SplitDoublePlayer("Human 1"), HitPlayer("Human 2"), RandomPlayer("Human 3")]
#players = [Player('Team Twitter')]
#players = [HitPlayer("Human 2")]
dealer = Dealer("Dealer")

# Initialize game object
game = Game(deck, dealer, players)
# Deal hands and have players place bets.
game.start_turn()

# GAME LOOP - retrieve player input until they have lost the round or are
# standing (I think)
turn_count = 0
while not game.over:
    # For each player at table, get actions, followed by dealer's action
    UI.player_hand(dealer, dealer.get_hand())

    for player in players:
        UI.player_info(player)

        hands_copy = player.hands[:]
        for hand in hands_copy:
            
            UI.hand_without_name(hand)
            # Get the player's action and act on it.
            action = player.get_action()
            game.accomodate_player_action(player, action, hand)

        UI.end_player_info_loop()
        # Split any hands that need splitting.

    game.split_player_hands()

    # Fold any hands that are invalid and end the players' turns.
    #game.validate_player_hands()

    # Get dealer action now that players have acted.
    dealer_action = dealer.get_action()
    game.accomodate_player_action(dealer, dealer_action, dealer.get_hand())

    # Check game state. Is everybody standing, surrendered, or over?
    players_finished = True
    for player in players:
        if not player.turn_over:
            players_finished = False
            break

    if players_finished:
        # Enter dealer loop until dealer is finished
        while not dealer.turn_over:
            action = dealer.get_action()
            game.accomodate_player_action(dealer, action, dealer.get_hand())

        # Turn is now over. Clean up the table and prepare for a new turn.
        game.end_turn()
        game.start_turn()
    else:
        # disallow first-turn actions. Move to start of game loop
        continue

    turn_count += 1

UI.end_game(turn_count)
