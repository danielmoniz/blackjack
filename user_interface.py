class UserInterface:
    """A class to output information (as well as ask for input) from the user."""


    def game_instructions(self):
        print "To {}, type {}".format('hit', 'hit')
        print "To {}, type {}".format('stand', 'stand')
        print "To {}, type {}".format('surrender', 'surrender')
        print "To {}, type {}".format('double down', 'double')
        print "To {}, type {}".format('split', 'split')
        print "To {}, type {}".format('exit', 'CTRL-C')
    
    def line_break(self):
        return  "--------------"

    def line_break_small(self):
        return  "-------"

    def line_break_tiny(self):
        return  "---"

    # ======================================================
    # play.py output

    def start_turn(self):
        print self.line_break()*3
        #print "NEW TURN"
        print self.line_break()*3

    def end_game(self, turn_count):
        print self.line_break()
        print "Game over! All players ran out of chips."
        print "The game lasted {} turns.".format(turn_count)

    def player_hand(self, player, player_hand):
        print self.line_break()
        print "{} hand:".format(player)
        print player_hand
        print player_hand.values()

    def hand_without_name(self, hand):
        print hand
        print hand.values()
        print self.line_break_tiny()

    def player_hand_fold(self, player, player_hand, hand_value):
        #print dealer_hand, dealer_hand.folded
        print "{} folded hand!".format(player), "Value", hand_value

    def player_hand_bet(self, player, hand):
        print self.line_break_small()
        print hand
        print hand.bet

    def player_info(self, player):
        print self.line_break_tiny(), player.chips, "CHIPS", self.line_break_tiny()
        print self.line_break(), player.name

    def end_player_info_loop(self):
        print "---------"

    # ======================================================
    # Game class output

    def player_score(self, player, player_score):
        print self.line_break_small()
        print "{} score:".format(player.name), player_score

    # ======================================================
    # Hand result output

    def win_hand(self, player, value):
        print str(player), "won", value, "chips!"

    def lose_hand(self, player, value):
        print str(player), "lost", value, "chips."

    def push_hand(self, player, value):
        print str(player), "broke even with", value, "chips."


    # =====================================================
    # Game result output

    def lose(self, player):
        print player, "loses!"

    # =====================================================
    # Action output

    def player_action(self, player, action):
        print "{} action:".format(player), action

    def deal_card(self, player, card):
        print "Dealt:", card

    def deal_hand(self, player, hand):
        print "Newly dealt cards:"
        print hand
        print self.line_break()

    def double_down_fail(self, player):
                print "Not enough chips for a double down! Hitting instead."


    # ====================================================
    # Miscelaneous

    def too_many_players(self, max_players):
            print "Cannot have more than {} players!".format(max_players)

    # ====================================================
    # User input

   
    def get_user_input(self):
        pass

    def get_integer_user_input(self):
        pass
