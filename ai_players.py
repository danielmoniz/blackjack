from player import Player
import random

class HitPlayer(Player):
    """A simple AI that hits every time."""

    def __str__(self):
        return "Hit Player"
    
    def get_user_input(self, message):
        """Return hit every time."""
        return 'hit'

class RandomPlayer(Player):
    """A simple AI that randomly chooses between hit and stand every time."""

    def __str__(self):
        return "Random Player"
    
    def get_user_input(self, message):
        """Return 'hit' every time."""
        if random.random() < 0.5:
            return 'hit'
        else:
            return 'stand'

class SplitDoublePlayer(Player):
    """A simple AI that splits whenever possible, doubles when it can't split
    on the first time, and stands otherwise."""

    def __str__(self):
        return "Split/Double Player"
    
    def get_user_input(self, message):
        """Return 'double' every time."""
        if self.first_turn:
            hand = self.hands[0]
            if hand.cards == 2:
                card1, card2 = hand.cards
                if card1.get_value() == card2.get_value():
                    return 'split'
            return 'double'
        else:
            return 'stand'
