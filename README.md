# Deck of Cards

A Python implementation of a standard 52-card poker deck with shuffle and dealing functionality.

## Features

- Standard 52-card deck (4 suits × 13 ranks)
- Custom shuffle algorithm (Fisher-Yates)
- Deal cards one at a time
- Reset deck functionality

## Installation

```bash
git clone https://github.com/Kamacho68/deck-of-cards-python.git
cd deck-of-cards
pip install -r requirements.txt
```

---

# Specification Document

## **Python Coding Challenge – Deck of Cards**

### **Objective**

Implement a Python solution to represent and manipulate a standard poker deck (52 playing cards).

### **Deck Details**

- **Suits**: Hearts, Spades, Clubs, Diamonds
- **Ranks**: Ace, 2–10, Jack, Queen, King
- Total: **52 unique cards**

---

### **Requirements**

#### **Class Structure**

- Create one or more Python classes to model the deck and its cards.
- At minimum, implement a `Deck` class.

---

### **Methods to Implement**

1. **`shuffle()`**
   - Randomizes the order of cards in the deck.
   - Must **not** use built-in shuffle utilities (e.g., `random.shuffle`).
   - You **may** use random number generators (e.g., `random.randint`).
   - Returns: `None`
2. **`deal_one_card()`**
   - Returns the **top card** from the deck.
   - If the deck is empty, return `None` (or equivalent).
   - After one `shuffle()` and 52 calls to `deal_one_card()`, all cards must be dealt exactly once, in random order.

---

### **Behaviour Expectations**

- The deck should start in a known, ordered state.
- Calling `shuffle()` changes the order randomly.
- Dealing cards reduces the deck size until empty.
- No duplicate cards should appear.

---

# Key Design decisions and Features

## Design Overview

**Two-Class Structure:**

- `Card`: Represents individual cards with suit and rank
- `Deck`: Manages the collection of 52 cards

## Key Features

**Requirements Met:**

1. ✅ **shuffle()**: Uses Fisher-Yates algorithm (no built-in shuffle)
2. ✅ **deal_one_card()**: Returns top card, removes it from deck, returns `None` when empty
3. ✅ **52 unique cards**: Hearts, Spades, Clubs, Diamonds × Ace through King
4. ✅ **Known initial order**: Cards created in predictable sequence
5. ✅ **Random dealing**: After shuffle + 52 deals, all cards appear exactly once

**Additional Useful Methods:**

- `cards_remaining()`: Check how many cards left
- `is_empty()`: Boolean check for empty deck
- `reset()`: Restore deck to initial 52-card state
- String representations for debugging

## Algorithm Details

**Shuffle Implementation:**

- Fisher-Yates shuffle algorithm ensures uniform randomness
- Each position has equal probability of containing any card
- Time complexity: O(n), Space complexity: O(1)

**Card Dealing:**

- Uses `pop()` from end of list (O(1) operation)
- "Top card" convention: last card in the list

The example code demonstrates dealing all 52 cards after shuffling and verifies that exactly 52 unique cards are dealt, meeting the specification perfectly.

---

# Complete project directory structure and testing guide

## Project Directory Structure

```
deck-of-cards/
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore patterns
├── src/                        # Source code package
│   ├── __init__.py             # Package initialization
│   ├── card.py                 # Card class implementation
│   └── deck.py                 # Deck class implementation
├── tests/                      # Test suite
│   ├── __init__.py             # Test package initialization
│   ├── test_card.py            # Unit tests for Card class
│   ├── test_deck.py            # Unit tests for Deck class
│   └── test_integration.py     # Integration tests
├── examples/                   # Demo and example code
│   ├── __init__.py             # Examples package initialization
│   └── demo.py                 # Demo script (with path handling)
├── htmlcov   # Coverage report folder (generated after running coverage tests)
└── venv                    # Virtual environment folder (created during setup)
```

1. **`venv/`** - Virtual environment folder (created during setup)
   - Contains isolated Python environment
   - Includes installed packages and executables
   - Keeps project dependencies separate from system Python
2. **`htmlcov/`** - Coverage report folder (generated after running coverage tests)
   - `index.html` - Interactive coverage dashboard
   - Individual `.html` files for each source module
   - CSS/JS assets for the web interface

## Setup Steps

### 1. Create Project Structure

```bash
# Create main directory
mkdir deck-of-cards
cd deck-of-cards

# Create subdirectories
mkdir src tests examples

# Create __init__.py files
touch src/__init__.py tests/__init__.py examples/__init__.py
```

### 2. Install Dependencies

```bash
# 1. Setup (one time)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. Development cycle
# ... make code changes ...

# 3: Install minimal testing dependencies only
pip install pytest pytest-cov

# 4. Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=html

# 5. View detailed coverage report
open htmlcov/index.html  # Opens interactive coverage dashboard

# 6. Run demo to verify functionality
python examples/demo.py
```

## Testing Steps

### Basic Testing

```bash
# Run all tests with verbose output
python -m pytest tests/ -v
```

_Expected output:_

```
====================================== test session starts =======================================
platform darwin -- Python 3.12.1, pytest-8.4.1, pluggy-1.6.0 -- /Users/myworkspace/Projects/deck-of-cards/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/myworkspace/Projects/deck-of-cards
plugins: cov-6.2.1
collected 18 items

tests/test_card.py::TestCard::test_card_creation PASSED                                    [  5%]
tests/test_card.py::TestCard::test_card_string_representation PASSED                       [ 11%]
tests/test_card.py::TestCard::test_card_repr PASSED                                        [ 16%]
tests/test_card.py::TestCard::test_card_equality PASSED                                    [ 22%]
tests/test_card.py::TestCard::test_card_hashable PASSED                                    [ 27%]
tests/test_deck.py::TestDeck::test_deck_initialization PASSED                              [ 33%]
tests/test_deck.py::TestDeck::test_deck_contains_all_cards PASSED                          [ 38%]
tests/test_deck.py::TestDeck::test_deal_one_card PASSED                                    [ 44%]
tests/test_deck.py::TestDeck::test_deal_from_empty_deck PASSED                             [ 50%]
tests/test_deck.py::TestDeck::test_reset_deck PASSED                                       [ 55%]
tests/test_deck.py::TestDeck::test_shuffle_changes_order PASSED                            [ 61%]
tests/test_deck.py::TestDeck::test_shuffle_preserves_all_cards PASSED                      [ 66%]
tests/test_deck.py::TestDeck::test_string_representation PASSED                            [ 72%]
tests/test_integration.py::TestIntegration::test_full_deck_deal_after_shuffle PASSED       [ 77%]
tests/test_integration.py::TestIntegration::test_multiple_shuffle_and_deal_cycles PASSED   [ 83%]
tests/test_integration.py::TestIntegration::test_shuffle_randomness_distribution PASSED    [ 88%]
tests/test_integration.py::TestIntegration::test_deck_order_after_reset PASSED             [ 94%]
tests/test_integration.py::TestIntegration::test_card_dealing_order PASSED                 [100%]

======================================= 18 passed in 0.04s =======================================
```

### Coverage Testing

```bash
# Run tests with coverage report
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term
```

_Expected output:_

```
====================================== test session starts =======================================
platform darwin -- Python 3.12.1, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/myworkspace/Projects/deck-of-cards
plugins: cov-6.2.1
collected 18 items

tests/test_card.py .....                                                                   [ 27%]
tests/test_deck.py ........                                                                [ 72%]
tests/test_integration.py .....                                                            [100%]

========================================= tests coverage =========================================
________________________ coverage: platform darwin, python 3.12.1-final-0 ________________________

Name          Stmts   Miss  Cover
---------------------------------
src/card.py      14      0   100%
src/deck.py      31      0   100%
---------------------------------
TOTAL            45      0   100%
Coverage HTML written to dir htmlcov
======================================= 18 passed in 0.14s =======================================
```

### Specific Test Categories

```bash
# Test individual components
python -m pytest tests/test_card.py -v          # Card class only
python -m pytest tests/test_deck.py -v          # Deck class only
python -m pytest tests/test_integration.py -v   # Integration tests only

# Test specific functionality
python -m pytest tests/test_deck.py::TestDeck::test_shuffle_changes_order -v
python -m pytest tests/test_integration.py::TestIntegration::test_full_deck_deal_after_shuffle -v
```

### Demo and Manual Testing

```bash
# Run demo to verify functionality
python examples/demo.py
```

_Expected output shows:_

- Deck creation and initial state
- Card dealing in order
- Shuffle functionality
- Random card dealing
- Full deck verification
- Statistics (cards per suit/rank)

```
=== Deck of Cards Demo ===

Created new deck: Deck with 52 cards remaining
Is empty: False

First 5 cards in order:
  1. King of Diamonds
  2. Queen of Diamonds
  3. Jack of Diamonds
  4. 10 of Diamonds
  5. 9 of Diamonds

Deck reset: Deck with 52 cards remaining
Deck shuffled!

First 5 cards after shuffle:
  1. 4 of Diamonds
  2. 10 of Clubs
  3. 9 of Spades
  4. Jack of Clubs
  5. 5 of Diamonds

Cards remaining: 47

Dealing a poker hand (5 cards):
  5 of Clubs
  Ace of Spades
  3 of Spades
  4 of Hearts
  King of Diamonds

Cards left in deck: 47

Dealing entire deck to verify uniqueness...
Total cards dealt: 52
Unique cards: 52

Cards per suit:
  Hearts: 13
  Spades: 13
  Clubs: 13
  Diamonds: 13

Cards per rank:
  Ace: 4
  2: 4
  3: 4
  4: 4
  5: 4
  6: 4
  7: 4
  8: 4
  9: 4
  10: 4
  Jack: 4
  Queen: 4
  King: 4

Dealing from empty deck: None
```

---

## Test Coverage Areas

### Unit Tests (test_card.py)

- ✅ Card creation with suit and rank
- ✅ String representations (**str**, **repr**)
- ✅ Equality comparison
- ✅ Hashability for sets/dictionaries

### Unit Tests (test_deck.py)

- ✅ Deck initialization (52 cards)
- ✅ All expected cards present
- ✅ Card dealing mechanics
- ✅ Empty deck handling
- ✅ Reset functionality
- ✅ Shuffle algorithm effectiveness
- ✅ Card preservation during shuffle

### Integration Tests (test_integration.py)

- ✅ Complete shuffle → deal → verify uniqueness cycle
- ✅ Multiple shuffle/deal cycles
- ✅ Statistical randomness verification
- ✅ Original order restoration after reset
- ✅ Dealing order (top of deck)

## Expected Test Results

**Successful run should show:**

- **15+ test cases** passing
- **100% code coverage** for core functionality
- **0 failures, 0 errors**
- Verification that all 52 unique cards are dealt exactly once after shuffle

**Key Integration Test Verifications:**

- Shuffle produces different order from original
- All 52 cards remain after shuffle (no loss/duplication)
- Complete deck dealing yields exactly 52 unique cards
- Multiple cycles maintain card integrity
- Statistical randomness in shuffle distribution

The test suite comprehensively validates both the individual components and the complete workflow specified in the original requirements.
