class Player:

    """Describes each player object in the game."""

    # @TODO
    def __init__(self, name = None):
        """Initialize chips and cards for a player."""
        # Other things might need to be initialized.
        self.name = name
        self.chips = 500
        self.cards = []
        self.turn_over = False
        self.actions = {
            'double': self.double_down, 
            'hit': self.hit, 
            'stand': self.stand, 
            'split': self.split, 
            'surrender': self.surrender
        # Track whether or not player has acted in a way that ends their turn.
        }

    def __str__(self):
        """Return the name of a player, or Player X if not set."""
        if self.name == None:
            return "Human player"

    def get_allowed_actions(self):
        """Return the actions currently available to the player."""
        return ['double', 'hit', 'stand', 'split', 'surrender']

    def get_action(self):
        """Get input from the player to determine their next action."""
        # input will require a loop until the player enters a valid action.
        return self.get_user_input("Type an action: ")

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
        print self.name, 'HIT' # Test output
        pass

    def stand(self):
        """Ie. end their turn (and wait)."""
        self.turn_over = True
        print self.name, 'STAND' # Test output
        pass

    def split(self):
        """If the two initial cards have the same value, separate them to make two hands."""
        print self.name, 'SPLIT' # Test output
        pass

    def surrender(self):
        """Give up a half-bet and retire from the game."""
        print self.name, 'SURRENDER' # Test output
        self.turn_over = True
        pass

    def get_user_input(self, message):
        user_input = raw_input(message)
        while user_input not in self.get_allowed_actions():
            print "Not an allowed action!"
            user_input = raw_input(message)

        return user_input

    def set_turn_over(self, status = True):
        self.turn_over = status
