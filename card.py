class Card:
    """Store information about a specific card and provide methods for
    retrieval."""

    def __init__(self, suit, value, name = None, face_up = True):
        """Store basic information about a card."""
        self.suit = suit
        self.value = value
        self.name = name
        self.face_up = face_up

    def get_value(self):
        """Return the value of the card."""
        return self.value

    def get_suit(self):
        """Return the suit of the card."""
        return self.suit

    def get_card_info(self):
        """Returns most information about a card in the form of a tuple:
        (suit, value, face_up)."""
        return (self.suit, self.value, self.face_up)

    def __str__(self):
        """Return a simple string representation of a card for ease of play.
        Returns basic card info if it is face up, and a notification o/w."""
        if self.face_up:
            return self.name, "of", self.suit + "s"
        else:
            return "Card is face down"

    def get_name(self):
        """Return the name of the card if it has one. If not, return its value.
        Eg. "the *Ace* of Spades", vs. "the 9 of Spades". <== name, value."""
        if name == None:
            return self.value
        else:
            return self.name
