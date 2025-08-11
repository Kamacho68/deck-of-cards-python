"""Demo script showing how to use the deck of cards."""

import sys
import os

# Add the parent directory to sys.path so we can import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.deck import Deck


def main():
    """Demonstrate deck functionality."""
    print("=== Deck of Cards Demo ===\n")
    
    # Create and show initial deck
    deck = Deck()
    print(f"Created new deck: {deck}")
    print(f"Is empty: {deck.is_empty()}")
    
    # Show first few cards in order
    print(f"\nFirst 5 cards in order:")
    temp_cards = []
    for i in range(5):
        card = deck.deal_one_card()
        temp_cards.append(card)
        print(f"  {i+1}. {card}")
    
    # Put cards back and reset for demo
    deck.reset()
    print(f"\nDeck reset: {deck}")
    
    # Shuffle and show randomized order
    deck.shuffle()
    print("Deck shuffled!")
    
    print(f"\nFirst 5 cards after shuffle:")
    for i in range(5):
        card = deck.deal_one_card()
        print(f"  {i+1}. {card}")
    
    print(f"\nCards remaining: {deck.cards_remaining()}")
    
    # Deal poker hand
    deck.reset()
    deck.shuffle()
    
    print(f"\nDealing a poker hand (5 cards):")
    poker_hand = []
    for i in range(5):
        card = deck.deal_one_card()
        poker_hand.append(card)
        print(f"  {card}")
    
    print(f"\nCards left in deck: {deck.cards_remaining()}")
    
    # Demonstrate full deck dealing
    deck.reset()
    deck.shuffle()
    
    print(f"\nDealing entire deck to verify uniqueness...")
    dealt_cards = []
    suits_count = {'Hearts': 0, 'Spades': 0, 'Clubs': 0, 'Diamonds': 0}
    ranks_count = {}
    
    while not deck.is_empty():
        card = deck.deal_one_card()
        dealt_cards.append(card)
        suits_count[card.suit] += 1
        ranks_count[card.rank] = ranks_count.get(card.rank, 0) + 1
    
    print(f"Total cards dealt: {len(dealt_cards)}")
    print(f"Unique cards: {len(set((c.suit, c.rank) for c in dealt_cards))}")
    
    print(f"\nCards per suit:")
    for suit, count in suits_count.items():
        print(f"  {suit}: {count}")
    
    print(f"\nCards per rank:")
    for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
        print(f"  {rank}: {ranks_count.get(rank, 0)}")
    
    # Test empty deck
    empty_card = deck.deal_one_card()
    print(f"\nDealing from empty deck: {empty_card}")


if __name__ == "__main__":
    main()