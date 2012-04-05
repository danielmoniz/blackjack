class Deck():
    def __init__(self):
# randomly generate cards here
        self.cards = []

    def get_next_card(self):
        """Return the next card in the deck."""
        pass

    def deal_initial_hands(self):
        """A wrapper for get_next_card. Deals hands for all players in the
        game.
        Deal two cards to each bet box starting from the dealer's left,
        followed by one for the dealer and one face down."""
        pass

    def deal_cards(self):
        """Deal a single card to each position that has a bet, clockwise from
        dealer's left, followed by a single card to the dealer. Then deal an initial card to each position in play."""
        pass

    def generate_deck(self):
        """A helper function to generate a deck."""
        pass

    def shuffle_deck(self):
        """Completely shuffles a deck."""
        pass


