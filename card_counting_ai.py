from player import Player

class SimpleBeatTheDealerPlayer(Player):
    """A simple AI that hits every time."""

    def __init__(self, name = None):
        """Have a variable for storing the game's count."""
        if name == None:
            name = "SimpleBeatTheDealer"
        Player.__init__(self, name)
        self.count = 0
        # Given the dealer's first card, outputs the lowest number at which the
        # player should stand if their hand is hard. Note that Aces here are
        # treated as 11, NOT 1.
        self.hard_standing_table = {
            2:13,
            3:13,
            4:12,
            5:12,
            6:12,
            7:17,
            8:17, 
            9:17, 
            10:17, 
            11:17
        }
        self.soft_standing_table = {
            2:18,
            3:18,
            4:18,
            5:18,
            6:18,
            7:18,
            8:18, 
            9:19, 
            10:19, 
            11:18
        }


    def __str__(self):
        return self.name
    
    def get_user_input(self, game, hand, message, allowed_actions):
        """Return an action given the game's count up until this point."""
        # @TODO This is a placeholder. Return a dynamic action instead.
        # NOTE: Cannot determine action until the player knows what is in the
        # dealer's hand!
        dealer_hand = game.dealer.get_hand()
        dealer_value = dealer_hand.largest_value()
        my_value = hand.largest_value()
        # @TODO In Beat The Dealer, the dealer draws cards only after everyone
        # is done. This is conditional is a simple hack to avoid extra logic.
        if dealer_value <= 11:
            if hand.is_hard():
                smallest_stand = self.hard_standing_table[dealer_value]
            else:
                smallest_stand = self.soft_standing_table[dealer_value]
        else:
            # Temporary. 
            smallest_stand = 1

        if my_value >= smallest_stand:
            return 'stand'
        else:
            return 'hit'

    def get_user_integer_input(self, game, hand, message, default, minimum, maximum):
        """Return a bet depending on the game's count, ie. how sure the player is that the draw will be favourable."""
        # @TODO Return a dynamic bet. Not immediately important.
        bet = default
        if self.count > 0:
            bet = self.count * default
        # @TODO The 'self.chips' part is a dirty hack. The Game class should be checking for whether or not a player has enough chips to bet!
        return min(bet, maximum, self.chips)

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
