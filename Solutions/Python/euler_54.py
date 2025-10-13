from collections import Counter

# Card values mapping
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
          'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def hand_rank(hand):
    """Return a tuple representing hand strength for comparison."""
    vals = sorted([values[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    counts = Counter(vals)
    count_vals = sorted(((cnt, val) for val, cnt in counts.items()), reverse=True)
    is_flush = len(set(suits)) == 1
    is_straight = vals == list(range(vals[0], vals[0]-5, -1))
    
    if is_straight and is_flush:
        return (8, vals[0])           # Straight flush
    if count_vals[0][0] == 4:
        return (7, count_vals[0][1], count_vals[1][1])  # Four of a kind
    if count_vals[0][0] == 3 and count_vals[1][0] == 2:
        return (6, count_vals[0][1], count_vals[1][1])  # Full house
    if is_flush:
        return (5, vals)              # Flush
    if is_straight:
        return (4, vals[0])           # Straight
    if count_vals[0][0] == 3:
        return (3, count_vals[0][1], sorted([v for v in vals if v != count_vals[0][1]], reverse=True))  # Three of a kind
    if count_vals[0][0] == 2 and count_vals[1][0] == 2:
        pair_vals = sorted([count_vals[0][1], count_vals[1][1]], reverse=True)
        kicker = [v for v in vals if v not in pair_vals]
        return (2, pair_vals, kicker) # Two pairs
    if count_vals[0][0] == 2:
        kicker = [v for v in vals if v != count_vals[0][1]]
        return (1, count_vals[0][1], kicker) # One pair
    return (0, vals)                  # High card

# Count player 1 wins
player1_wins = 0
with open("poker.txt") as f:
    for line in f:
        cards = line.strip().split()
        hand1 = cards[:5]
        hand2 = cards[5:]
        if hand_rank(hand1) > hand_rank(hand2):
            player1_wins += 1

print(f"Player 1 wins {player1_wins} hands.")
