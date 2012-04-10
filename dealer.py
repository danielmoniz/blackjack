from player import Player

class Dealer(Player):

    def __init__(self, name = None):
        Player.__init__(self, name)
        self.chips = float("inf")

    def __str__(self):
        """Return some string representation for the dealer, eg. 'Dealer'."""
        return "Dealer"

    def get_allowed_actions(self):
        """Return the allowed actions for the dealer. Note that they cannot
        split, double, or surrender at any time."""
        return ['hit', 'stand']

    def get_action(self):
        """Given the dealer's current hand situation, return the required action."""
        if self.get_hand_value < 17:
            return 'hit'
        else:
            return 'stand'

    def get_hand(self):
        """Return the dealer's hand. If he does not have one, return False."""
        try:
            return self.hands[0]
        except KeyError:
            return False
