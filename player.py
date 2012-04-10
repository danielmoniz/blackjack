from hand import Hand
class Player:

    """Describes each player object in the game."""

    # @TODO
    def __init__(self, name = None):
        """Initialize chips and cards for a player."""
        # Other things might need to be initialized.
        self.name = name
        self.chips = 500
        self.hands = []
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

    # NOTE: This function is to be deprecated for a more dynamic funciton that
    # allows for a specific hand to be given a new card, not just a player.
    def assign_new_card(self, new_card, hand = None):

        # If player has no hands, create one.
        if len(self.hands) == 0:
            self.hands.append(Hand([new_card]))
        # If player has exactly one hand, use it.
        elif len(self.hands) == 1:
            self.hands[0].add_card(new_card)
        else:
            # if no hand is specified and player has >1 hands, return False.
            # This assumes hands is a non-negative integer.
            if hand == None:
                return False
            hand.add_card(new_card)
        return True

    def assign_hand(self, hand):
        """Deal a new hand to the player."""
        #for hand in 
        self.hands.append(hand)

    def purge_hands(self):
        """Remove all hands for this player."""
        del self.hands[:]

    # @TODO This may not be necessary!
    def validate_hands(self):
        """Check if any of the player's hands are invalid. If so, push their chips to the dealer."""
        pass

    def get_hand_value(self, hand):
        """Add up the cards in play and return their value."""
        hand_sum = 0
        for card in hand:
            hand_sum += card.get_value()
        return hand_sum

    def get_action(self):
        """Get input from the player to determine their next action."""
        # input will require a loop until the player enters a valid action.
        return self.get_user_input("Type an action: ")

    def fold_hand(self, hand):
        """Remove a hand from play."""
        hand.fold()
        return True

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
        self.set_turn_over()
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

    # @TODO Make this do something.
    def place_bet(self, size_of_bet, hand = None):
        """Makes a player place a bet on a specific hand that belongs to them.
        If no hand is provided, it defaults to their first hand."""
        pass


    def get_user_input(self, message):
        user_input = raw_input(message)
        while user_input not in self.get_allowed_actions():
            print "Not an allowed action!"
            user_input = raw_input(message)

        return user_input

    def set_turn_over(self, status = True):
        self.turn_over = status
