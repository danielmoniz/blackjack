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
        
deck = Deck()
deck.shuffle()
# For now, create a single player. Should allow for more.
players = [Player("Human 1")]
dealer = Dealer("Dealer")

# Initialize game object
game = Game(deck, dealer, players)
game.start_turn()

# GAME LOOP - retrieve player input until they have lost the round or are
# standing (I think)
while not game.over:
    # For each player at table, get actions, followed by dealer's action
    print "-------------"
    # Dealer only has one hand! Print out its information.
    print "Dealer hand:"
    print dealer.get_hand()
    print dealer.get_hand().values()
    for player in players:
        print "---", player.chips, "CHIPS ---"
        print "---------", player.name
        for hand in player.hands:
            print hand
            print hand.values()
            print "--"
        print "---------"
        action = player.get_action()
        player.perform_action(action)
        game.accomodate_player_action(player, action)
    game.validate_player_hands()

    # Get dealer action now that players have acted.
    dealer_action = dealer.get_action()
    dealer.perform_action(dealer_action)
    game.accomodate_player_action(dealer, action)

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
            print "dealer action:", action
            dealer.perform_action(action)
            game.accomodate_player_action(dealer, action)
        game.validate_dealer_hand()

        # Turn is now over. Clean up the table and prepare for a new turn.
        game.end_turn()
        game.start_turn()
    else:
        # disallow first-turn actions. Move to start of loop
        continue
