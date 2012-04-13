from player import Player

class SimpleBeatTheDealerPlayer(Player):
    """A simple AI that hits every time."""

    def __init__(self, name = None):
        """Have a variable for storing the game's count."""
        if name == None:
            name = "SimpleBeatTheDealer"
        Player.__init__(self, name)
        self.count = 0

    def __str__(self):
        return self.name
    
    def get_user_input(self, message, allowed_actions):
        """Return an action given the game's count up until this point."""
        # @TODO This is a placeholder. Return a dynamic action instead.
        return 'hit'

    def get_user_integer_input(self, message, default, minimum, maximum):
        """Return a bet depending on the game's count, ie. how sure the player is that the draw will be favourable."""
        # @TODO Return a dynamic bet. Not immediately important.
        bet = default
        if self.count > 0:
            bet = self.count * default
        return min(bet, maximum)

    def show_card(self, card):
        """Override the Player function which shows a card to each player. Depending on which cards are shown, modify the game's "count"."""
        value = card.get_value()
        # This defines high, low, and middle cards
        if value >= 10 or value == 1:
            self.count_high_card()
        elif 2 <= value <= 6:
            self.count_low_card()
        else:
            # We don't count cards in the middle.
            pass
        pass

    def count_high_card(self):
        self.count -= 1

    def count_low_card(self):
        self.count += 1

    def get_action_from_count(self):
        pass
