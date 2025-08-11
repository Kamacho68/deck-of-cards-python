"""Deck class for managing a collection of playing cards."""

import random
from .card import Card


class Deck:
    """Represents a standard 52-card poker deck."""
    
    SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self):
        """Initialize deck with all 52 cards in standard order."""
        self.cards = []
        self._initialize_deck()
    
    def _initialize_deck(self):
        """Create all 52 cards in a known, ordered state."""
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        """
        Randomizes the order of cards using Fisher-Yates shuffle algorithm.
        Does not use built-in shuffle utilities.
        Returns: None
        """
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    
    def deal_one_card(self):
        """
        Returns the top card from the deck and removes it.
        Returns None if deck is empty.
        """
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
    
    def cards_remaining(self):
        """Returns the number of cards remaining in the deck."""
        return len(self.cards)
    
    def is_empty(self):
        """Returns True if deck is empty, False otherwise."""
        return len(self.cards) == 0
    
    def reset(self):
        """Resets the deck to initial state with all 52 cards."""
        self._initialize_deck()
    
    def __str__(self):
        """String representation showing remaining cards count."""
        return f"Deck with {len(self.cards)} cards remaining"
    
    def __len__(self):
        """Returns number of cards in deck."""
        return len(self.cards)