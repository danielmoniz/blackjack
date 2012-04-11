class UserInterface:
    """A class to output information (as well as ask for input) from the user."""

    def line_break(self):
        return  "--------------"

    def line_break_small(self):
        return  "-------"

    def line_break_tiny(self):
        return  "---"

    def start_loop(self):
        print self.line_break()*3
        print "NEW TURN"
        print self.line_break()*3

    def end_game(self, turn_count):
        print self.line_break()
        print "Game over! All players ran out of chips."
        print "The game lasted {} turns.".format(turn_count)

    def dealer_hand(self, dealer_hand):
        print self.line_break()
        print "Dealer hand:"
        print dealer_hand
        print dealer_hand.values()

    def player_info(self, player):
        print self.line_break_tiny, player.chips, "CHIPS", self.line_break_tiny
        print self.line_break, player.name

    def hand_info(self, hand):
        print hand
        print hand.values()
        print self.line_break_tiny()

    def end_player_info_loop(self):
        print "---------"

    def dealer_action(self, action):
        print "dealer action:", action
