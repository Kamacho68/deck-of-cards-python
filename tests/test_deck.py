"""Tests for the Deck class."""

import pytest
import random
from src.deck import Deck
from src.card import Card


class TestDeck:
    """Test cases for Deck class."""
    
    def test_deck_initialization(self):
        """Test deck is initialized with 52 cards."""
        deck = Deck()
        assert len(deck) == 52
        assert deck.cards_remaining() == 52
        assert not deck.is_empty()
    
    def test_deck_contains_all_cards(self):
        """Test deck contains all expected cards."""
        deck = Deck()
        
        # Check we have all suits and ranks
        suits = set()
        ranks = set()
        
        for card in deck.cards:
            suits.add(card.suit)
            ranks.add(card.rank)
        
        assert suits == set(Deck.SUITS)
        assert ranks == set(Deck.RANKS)
        
        # Check for exactly 52 unique cards
        unique_cards = set((card.suit, card.rank) for card in deck.cards)
        assert len(unique_cards) == 52
    
    def test_deal_one_card(self):
        """Test dealing a single card."""
        deck = Deck()
        initial_count = len(deck)
        
        card = deck.deal_one_card()
        
        assert card is not None
        assert isinstance(card, Card)
        assert len(deck) == initial_count - 1
    
    def test_deal_from_empty_deck(self):
        """Test dealing from empty deck returns None."""
        deck = Deck()
        
        # Deal all cards
        while not deck.is_empty():
            deck.deal_one_card()
        
        # Try to deal from empty deck
        card = deck.deal_one_card()
        assert card is None
        assert deck.is_empty()
    
    def test_reset_deck(self):
        """Test resetting deck restores all cards."""
        deck = Deck()
        
        # Deal some cards
        for _ in range(10):
            deck.deal_one_card()
        
        assert len(deck) == 42
        
        # Reset deck
        deck.reset()
        assert len(deck) == 52
        assert not deck.is_empty()
    
    def test_shuffle_changes_order(self):
        """Test that shuffle changes the order of cards."""
        deck = Deck()
        original_order = [str(card) for card in deck.cards]
        
        # Set random seed for reproducible test
        random.seed(42)
        deck.shuffle()
        shuffled_order = [str(card) for card in deck.cards]
        
        # Orders should be different (very high probability)
        assert original_order != shuffled_order
    
    def test_shuffle_preserves_all_cards(self):
        """Test that shuffle doesn't lose or duplicate cards."""
        deck = Deck()
        original_cards = set((card.suit, card.rank) for card in deck.cards)
        
        deck.shuffle()
        shuffled_cards = set((card.suit, card.rank) for card in deck.cards)
        
        assert original_cards == shuffled_cards
        assert len(deck) == 52
    
    def test_string_representation(self):
        """Test string representation of deck."""
        deck = Deck()
        assert str(deck) == "Deck with 52 cards remaining"
        
        deck.deal_one_card()
        assert str(deck) == "Deck with 51 cards remaining"