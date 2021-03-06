from card import Card
from user_interface import UserInterface

UI = UserInterface()

class Hand:
    """Defines a single hand. Also stores bets placed on a given hand, and who placed those bets."""
    
    def __init__(self, cards = None, bet = None):
        """'cards' is a list of cards (card objects) in the hand.
        'bets' is a tuple as follows: (bet_value, bet_owner).
        'split' indicates whether a hand should be split when possible."""
        if cards == None:
            self.cards = []
        else:
            self.cards = cards
        self.bet = bet
        self.folded = False
        self.split = False

    def __str__(self):
        """Returns a reasonable string representation of the hand."""
        output = ""
        card_string_list = [str(card) for card in self.cards]
        output = "\n".join(card_string_list)
        return output

    def add_card(self, new_card):
        """Adds a card to a hand."""
        self.cards.append(new_card)

    # @TODO This should be done with a list of bets, not a single bet.
    def place_bet(self, value, player):
        """Place a bet from the given player of the given chips value."""
        self.bet = (value, player)

    def clear_bet(self):
        """Removes the bet from a hand."""
        self.bet = None

    def values(self):
        """Add up the cards in play and return their highest and lowest values
        tuple form. That is, if there are n aces in the hand, the tuple will be
        of size n+1 and will include n+1 different hand values."""

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
        valid_values = [value for value in self.values() if value <= 21]
        if len(valid_values) == 0:
            # Return any value > 21. min(values) works fine.
            return min(self.values())
        # Return the maximum value that is <= 21.
        return max(valid_values)

    def fold(self):
        """Folds a hand. Simply makes it inactive for later cleanup."""
        self.folded = True

    def validate(self):
        """Fold the hand if it is invalid.
        Return True if valid, False if invalid."""
        if self.smallest_value() > 21:
            #print "folded hand. value", self.smallest_value()
            #UI.player_hand_fold()
            self.fold()
            return False

        return True

    def is_blackjack(self):
        """Return True if the hand is made up of exactly one one Ace and a face card. Returns False otherwise.
        Two conditions to being a blackjack:
            1. There are exactly two cards.
            2. The maximum value of the cards adds up to 21."""
        if len(self.cards) == 2 and self.largest_value() == 21:
            return True
        return False

    def is_hard(self):
        """Returns True if a hand has no aces, and False otherwise."""
        for card in self.cards:
            # If the card is an Ace, the hand must be soft.
            if card.get_value() == 1:
                return False
        return True

    def num_cards(self):
        """Return the number of cards in the hand."""
        return len(self.cards)

    def prepare_split(self):
        """Indicate that the hand should be split when possible."""
        self.split = True

    def unsplit(self):
        """Indicate that the hand should be split when possible."""
        self.split = False

    def get_bet_value(self):
        """Return the chip value of the bet."""
        return self.bet[0]

    def get_bet_owner(self):
        """Return the owner of the bet."""
        return self.bet[1]
