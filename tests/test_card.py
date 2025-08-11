"""Tests for the Card class."""

import pytest
from src.card import Card


class TestCard:
    """Test cases for Card class."""
    
    def test_card_creation(self):
        """Test creating a card with suit and rank."""
        card = Card('Hearts', 'Ace')
        assert card.suit == 'Hearts'
        assert card.rank == 'Ace'
    
    def test_card_string_representation(self):
        """Test string representation of card."""
        card = Card('Spades', 'King')
        assert str(card) == 'King of Spades'
    
    def test_card_repr(self):
        """Test repr representation of card."""
        card = Card('Clubs', 'Queen')
        assert repr(card) == "Card('Clubs', 'Queen')"
    
    def test_card_equality(self):
        """Test card equality comparison."""
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Hearts', 'Ace')
        card3 = Card('Hearts', 'King')
        card4 = Card('Spades', 'Ace')
        
        assert card1 == card2
        assert card1 != card3
        assert card1 != card4
        assert card1 != "not a card"
    
    def test_card_hashable(self):
        """Test that cards can be used in sets and as dict keys."""
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Hearts', 'Ace')
        card3 = Card('Spades', 'Ace')
        
        card_set = {card1, card2, card3}
        assert len(card_set) == 2  # card1 and card2 are the same
        
        card_dict = {card1: 'value1', card3: 'value2'}
        assert len(card_dict) == 2