from player import Player

class Dealer(Player):

    def __init__(self):
        Player.__init__(self)
        self.chips = float("inf")

    def get_allowed_actions(self):
        """Return the allowed actions for the dealer. Note that they cannot
        split, double, or surrender at any time."""
        return ['hit', 'stand']

    def get_action(self):
        """Given the dealer's current hand situation, return the required action."""
        if self.get_total_card_value < 17:
            return 'hit'
        else:
            return 'stand'
