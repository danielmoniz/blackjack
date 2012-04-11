from card import Card
import random

class Deck:
    def __init__(self, num_decks = 2, discard = None):
        """Randomly generate a deck of the given size."""
        self.suits = ['hearts', 'clubs', 'spades', 'diamonds']
        self.cards_per_suit = 13
        if discard == None:
            self.discard_pile = []
        else:
            self.discard_pile = discard
        
        self.cards = self.generate_deck(num_decks)

    def get_next_card(self):
        """Return the next card in the deck and remove it."""
        if self.get_num_cards() == 0:
            self.cards = self.discard_pile[:]
            del self.discard_pile[:]
            for card in self.cards:
                card.flip()
            self.shuffle()
            # @TODO RESHUFFLE all cards in discard pile? Need to make a discard pile!
        next_card = self.cards.pop()
        # Cards in a deck are flipped down, so they must be flipped.
        next_card.flip()
        return next_card

    def discard(self, card):
        """Adds a card to the discard pile."""
        self.discard_pile.append(card)

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

    # DEPRECATED
    def add_card(self, card):
        """Places a card on TOP of the deck. Mainly used for discard piles. It is not flipped automatically."""
        self.cards.append(card)
