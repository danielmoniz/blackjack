class Player:
    """Describes each player object in the game."""

    # @TODO
    def __init__(self):
        """Initialize chips and cards for a player."""
        # Other things might need to be initialized.
        self.chips = 500
        self.cards = []
        self.actions = {
            'double': self.double_down, 
            'hit': self.hit, 
            'stand': self.stand, 
            'split': self.split, 
            'surrender': self.surrender
        }

    def get_allowed_actions(self):
        """Return the actions currently available to the player."""
        return ['double', 'hit', 'stand', 'split', 'surrender']

    def get_action(self):
        """Get input from the player to determine their next action."""
        # input will require a loop until the player enters a valid action.
        pass

    def get_total_card_value(self):
        """Add up the cards in play and return their value."""
        return sum(self.cards)

    def perform_action(self, action):
        """Take in an action and act on it."""
        return self.actions[action]()

# FUNCTIONS FOR ACTIONS A PLAYER CAN TAKE
    def double_down(self):
        """Double wager, take a single card and finish."""
        pass

    def hit(self):
        """Ie. take a card."""
        pass

    def stand(self):
        """Ie. end their turn (and wait)."""
        pass

    def split(self):
        """If the two initial cards have the same value, separate them to make two hands."""
        pass

    def surrender(self):
        """Give up a half-bet and retire from the game."""
        pass


