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
        """Given the dealer's current hand situation, return the required
        action. The dealer stands if any of his hand values are 17 or over."""
        for value in self.get_hand().values():
            # If any value is greater than 17
            if 17 <= value <= 21:
                return 'stand'
        # This case ensures that if the dealer is over 21 in all cases, he
        # stops
        if self.get_hand().smallest_value() > 21:
            return 'stand'
        return 'hit'

    def get_hand(self):
        """Return the dealer's hand. If he does not have one, return False."""
        try:
            return self.hands[0]
        except KeyError:
            return False
