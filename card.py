class Card:
    """Store information about a specific card and provide methods for
    retrieval."""

    def __init__(self, suit, value, face_up = True, name = None):
        """Store basic information about a card."""
        self.suit = suit
        self.value = value
        self.name = name
        self.face_up = face_up

    def __str__(self):
        """Return a simple string representation of a card for ease of play.
        Returns basic card info if it is face up, and a notification o/w."""
        if self.face_up:
            return self.get_name() + " of " + self.suit
        else:
            return "Card is face down"

    def get_value(self):
        """Return the value of the card."""
        if self.value > 10:
            return 10
        return self.value

    def flip(self):
        self.face_up = not self.face_up
        return self.face_up

    def get_suit(self):
        """Return the suit of the card."""
        return self.suit

    def get_card_info(self):
        """Returns most information about a card in the form of a tuple:
        (suit, value, face_up)."""
        return (self.suit, self.value, self.face_up)

    def get_name(self):
        """Return the name of the card if it has one. If not, return its value.
        Eg. "the *Ace* of Spades", vs. "the 9 of Spades". <== name, value."""
        if self.name == None:
            self.name = self.get_name_from_value(self.value)
            return str(self.name)
        else:
            return str(self.name)

    def get_name_from_value(self, value):
        """Take in an integer value for a card and output its name.
        Note that an Ace can take the value of 14 as well, since King is 13.
        Note also that Jack, Queen, and King have the value 10, NOT 11, 12, and
        13!!"""
        names = {1: 'Ace', 14: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
        return names[value]
