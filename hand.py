from card import Card

class Hand:
    """Defines a single hand. Also stores bets placed on a given hand, and who placed those bets."""
    
    def __init__(self, cards = None, bets = []):
        """'cards' is a list of cards (card objects) in the hand.
        'bets' is a list of tuples as follows: (bet_value, bet_owner)."""
        if cards == None:
            self.cards = []
        else:
            self.cards = cards
        self.bets = bets
        self.folded = False

    def __str__(self):
        """Returns a reasonable string representation of the hand."""
        output = ""
        card_string_list = [str(card) for card in self.cards]
        output = "\n".join(card_string_list)
        return output

    def add_card(self, new_card):
        """Adds a card to a hand."""
        self.cards.append(new_card)
        return True

    def values(self):
        """Add up the cards in play and return their highest and lowest values tuple form. That is, if there are n aces in the hand, the tuple will be of size n and will include n different hand values."""

        num_aces = 0
        for card in self.cards:
            if card.get_value() == 1:
                num_aces += 1
        values = []
        for i in range(0, num_aces + 1):
            # We count the number of aces i being used as high values
            hand_sum = 11*i + 1*(num_aces - i)
            for card in self.cards:
                # Ignore aces! We've added those separately.
                if card.get_value() != 1:
                    hand_sum += card.get_value()
            values.append(hand_sum)

        return tuple(values)

    def smallest_value(self):
        """Wrap the values() method to return the smallest possible hand value."""
        return self.values()[0]

    def largest_value(self):
        """Wrap the values() method to return the largest possible hand value."""
        return self.values()[-1]

    def best_value(self):
        """Wrap the values() method to return the value that is closest to 21
        without being over."""
        valid_values = [value for value in self.values if value <= 21]
        return max(valid_values)

    def fold(self):
        """Fold a hand. Simply makes it inactive for later cleanup."""
        self.folded = True
