from card import Card

class Hand:
    """Defines a single hand. Also stores bets placed on a given hand, and who placed those bets."""
    
    def __init__(self, cards = [], bets = []):
        """'cards' is a list of cards (card objects) in the hand.
        'bets' is a list of tuples as follows: (bet_value, bet_owner)."""
        self.cards = cards
        self.bets = bets

    def add_card(self, new_card):
        """Adds a card to a hand."""
        self.cards.append(new_card)
        return True

    def values(self):
        """Add up the cards in play and return their highest and lowest values tuple form. That is, if there are n aces in the hand, the tuple will be of size n and will include n different hand values."""

        num_aces = 0
        values = []
        for card in self.cards:
            if card.get_value() == 1:
                num_aces += 1
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

    def smallest_value(self):
        """Wrap the values() method to return the smallest possible hand value."""
        return self.values()[-1]
