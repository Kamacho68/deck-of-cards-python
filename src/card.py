"""Card class for representing individual playing cards."""


class Card:
    """Represents a single playing card with suit and rank."""
    
    def __init__(self, suit, rank):
        """
        Initialize a card with suit and rank.
        
        Args:
            suit (str): The suit of the card
            rank (str): The rank of the card
        """
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        """Return string representation of card."""
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        """Return detailed string representation for debugging."""
        return f"Card('{self.suit}', '{self.rank}')"
    
    def __eq__(self, other):
        """Check equality with another card."""
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.rank == other.rank
    
    def __hash__(self):
        """Make card hashable for use in sets and as dict keys."""
        return hash((self.suit, self.rank))