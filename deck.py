from card import Card
import random

class Deck:
    def __init__(self, num_decks = 2):
# randomly generate cards here
        self.suits = ['hearts', 'clubs', 'spaces', 'diamonds']
        self.cards_per_suit = 13
        # ^^^ relies on suits being set
        self.cards = self.generate_deck(num_decks)

    def get_next_card(self):
        """Return the next card in the deck and remove it."""
        next_card = self.cards.pop()
        next_card.flip()
        return next_card
    
    def get_num_cards(self):
        """Return the total number of cards left in the deck."""
        return len(self.cards)

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

    def generate_deck(self, num_decks):
        """A helper function to generate a deck."""
        pass
        cards = []
        # For each deck, create a card in each suit at each value.
        for i in range(num_decks):
            for suit in self.suits:
                for value in range(1, self.cards_per_suit + 1):
                    cards.append(Card(suit, value, False))

        return cards

    def shuffle(self):
        """Completely shuffles a deck. Returns nothing."""
        random.shuffle(self.cards)
        return True
