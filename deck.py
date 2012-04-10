from card import Card
import random

class Deck:
    def __init__(self, num_decks = 2):
        """Randomly generate a deck of the given size."""
        self.suits = ['hearts', 'clubs', 'spades', 'diamonds']
        self.cards_per_suit = 13
        
        self.cards = self.generate_deck(num_decks)

    def get_next_card(self):
        """Return the next card in the deck and remove it."""
        if self.get_num_cards() == 0:
            pass
            # @TODO
            # RESHUFFLE all cards in discard pile? Need to make a discard pile!
        next_card = self.cards.pop()
        # Cards in a deck are flipped down, so they must be flipped.
        next_card.flip()
        return next_card

    def generate_deck(self, num_decks):
        """A helper function to generate a deck."""
        cards = []
        # For each deck, create a card in each suit at each value.
        for i in range(num_decks):
            for suit in self.suits:
                for value in range(1, self.cards_per_suit + 1):
                    cards.append(Card(suit, value, False))

        return cards

    def shuffle(self):
        """Completely shuffles a deck in place. Returns nothing."""
        random.shuffle(self.cards)
    
    def get_num_cards(self):
        """Return the total number of cards left in the deck."""
        return len(self.cards)
