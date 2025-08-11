"""Integration tests for the complete deck functionality."""

import pytest
from collections import Counter
from src.deck import Deck


class TestIntegration:
    """Integration test cases."""
    
    def test_full_deck_deal_after_shuffle(self):
        """Test dealing all 52 cards after shuffle produces unique cards."""
        deck = Deck()
        deck.shuffle()
        
        dealt_cards = []
        
        # Deal all cards
        while not deck.is_empty():
            card = deck.deal_one_card()
            dealt_cards.append(card)
        
        # Should have exactly 52 cards
        assert len(dealt_cards) == 52
        
        # All cards should be unique
        unique_cards = set((card.suit, card.rank) for card in dealt_cards)
        assert len(unique_cards) == 52
        
        # Should contain all expected combinations
        expected_combinations = set()
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                expected_combinations.add((suit, rank))
        
        assert unique_cards == expected_combinations
    
    def test_multiple_shuffle_and_deal_cycles(self):
        """Test multiple shuffle and deal cycles."""
        deck = Deck()
        
        for cycle in range(5):
            deck.reset()
            deck.shuffle()
            
            dealt_cards = []
            while not deck.is_empty():
                card = deck.deal_one_card()
                dealt_cards.append(card)
            
            # Each cycle should deal exactly 52 unique cards
            assert len(dealt_cards) == 52
            unique_cards = set((card.suit, card.rank) for card in dealt_cards)
            assert len(unique_cards) == 52
    
    def test_shuffle_randomness_distribution(self):
        """Test that shuffle produces reasonably random distribution."""
        # This test checks that the first card position
        # gets different cards across multiple shuffles
        deck = Deck()
        first_cards = []
        
        for _ in range(100):
            deck.reset()
            deck.shuffle()
            first_card = deck.cards[0] if deck.cards else None
            if first_card:
                first_cards.append((first_card.suit, first_card.rank))
        
        # Should have reasonable variety in first position
        unique_first_cards = set(first_cards)
        
        # We expect at least 20 different cards in first position out of 100 shuffles
        # This is a probabilistic test - very unlikely to fail with true randomness
        assert len(unique_first_cards) >= 20
    
    def test_deck_order_after_reset(self):
        """Test that deck returns to original order after reset."""
        deck1 = Deck()
        original_order = [(card.suit, card.rank) for card in deck1.cards]
        
        # Shuffle and deal some cards
        deck1.shuffle()
        for _ in range(20):
            deck1.deal_one_card()
        
        # Reset deck
        deck1.reset()
        reset_order = [(card.suit, card.rank) for card in deck1.cards]
        
        # Should match original order
        assert reset_order == original_order
    
    def test_card_dealing_order(self):
        """Test that cards are dealt from the top of the deck."""
        deck = Deck()
        
        # Get the last card (top of deck)
        expected_top_card = deck.cards[-1]
        
        # Deal one card
        dealt_card = deck.deal_one_card()
        
        # Should be the same card
        assert dealt_card.suit == expected_top_card.suit
        assert dealt_card.rank == expected_top_card.rank