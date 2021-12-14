"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie,
for example, both players have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
	 	2C 3S 8S 8D TD
Pair of Eights
	 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
	 	2C 5C 7D 8S QH
Highest card Queen
	 	Player 1
3	 	2D 9C AS AH AC
Three Aces
	 	3D 6D 7D TD QD
Flush with Diamonds
	 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
	 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
	 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
	 	3C 3D 3S 9S 9D
Full House
with Three Threes
	 	Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains
ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. Y
ou can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific
order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from collections import defaultdict

debug = True

class Hand:
    class Card:
        def __init__(self, value, suite):
            self.value = value
            self.suite = suite

        def rank(self):
            if self.value.isdigit():
                return int(self.value)
            elif self.value == 'T':
                return 10
            elif self.value == 'J':
                return 11
            elif self.value == 'Q':
                return 12
            elif self.value == 'K':
                return 13
            elif self.value == 'A':
                return 14
            else:
                raise ValueError('Unknown value {}'.format(self.value))

        def __str__(self):
            return '{}{}'.format(self.value, self.suite)

    def __init__(self, encoded_cards):
        self.cards = []
        for encoded_card in encoded_cards:
            self.cards.append(Hand.Card(encoded_card[0], encoded_card[1]))
        self.cards = sorted(self.cards, key=lambda c: c.rank())

    def __str__(self):
        return ' '.join((str(c) for c in self.cards))

    def _is_royal_flush(self):
        return {c.value for c in self.cards} == {'T', 'J', 'Q', 'K', 'A'}, 13

    def _is_straight_flush(self):
        return len({c.suite for c in self.cards}) == 1 and \
               {self.cards[i].rank() - self.cards[i-1].rank() for i in range(1, len(self.cards))} == {1}, self.cards[-1].rank()

    def _is_four_of_kind(self):
        d = self._group_by_count()
        for k, v in d.items():
            if v == 4:
                return True, Hand.Card(k, '').rank()
        return False, 0

    def _is_full_house(self):
        d = self._group_by_count()
        triple_rank, pair_rank = 0, 0
        for k, v in d.items():
            if v == 3:
                triple_rank = Hand.Card(k, '').rank()
            elif v == 2:
                pair_rank = Hand.Card(k, '').rank()
        return triple_rank > 0 and pair_rank > 0, triple_rank

    def _is_flush(self):
        return len({c.suite for c in self.cards}) == 1, self.cards[-1].rank()

    def _is_straight(self):
        return {self.cards[i].rank() - self.cards[i - 1].rank() for i in range(1, len(self.cards))} == {1}, \
               self.cards[-1].rank()

    def _is_three_of_kind(self):
        d = self._group_by_count()
        for k, v in d.items():
            if v == 3:
                return True, Hand.Card(k, '').rank()
        return False, 0

    def _is_two_pairs(self):
        d = self._group_by_count()
        pair1_rank, pair2_rank = 0, 0
        for k, v in d.items():
            if v == 2 and pair1_rank == 0:
                pair1_rank = Hand.Card(k, '').rank()
            elif v == 2 and pair2_rank == 0:
                pair2_rank = Hand.Card(k, '').rank()
        return pair1_rank > 0 and pair2_rank > 0, max(pair1_rank, pair2_rank)

    def _is_one_pair(self):
        d = self._group_by_count()
        for k, v in d.items():
            if v == 2:
                return True, Hand.Card(k, '').rank()
        return False, 0

    def _is_high_card(self):
        return True, self.cards[-1].rank()

    def _group_by_count(self):
        d = defaultdict(lambda: 0)
        for c in self.cards:
            d[c.value] += 1
        return d

    def rank(self):
        if self._is_royal_flush()[0]:
            if debug:
                print('royal flush')
            return 90_000 + self.cards[-1].rank()
        elif self._is_straight_flush()[0]:
            if debug:
                print('straight flush', self._is_straight_flush()[1])
            return 80_000 + self._is_straight_flush()[1] * 100 + self.cards[-1].rank()
        elif self._is_four_of_kind()[0]:
            if debug:
                print('four of a kind', self._is_four_of_kind()[1])
            return 70_000 + self._is_four_of_kind()[1] * 100 + self.cards[-1].rank()
        elif self._is_full_house()[0]:
            if debug:
                print('full house', self._is_full_house()[1])
            return 70_000 + self._is_full_house()[1] * 100 + self.cards[-1].rank()
        elif self._is_flush()[0]:
            if debug:
                print('flush', self._is_flush()[1])
            return 60_000 + self._is_flush()[1] * 100 + self.cards[-1].rank()
        elif self._is_straight()[0]:
            if debug:
                print('straight', self._is_straight()[1])
            return 50_000 + self._is_straight()[1] * 100 + self.cards[-1].rank()
        elif self._is_three_of_kind()[0]:
            if debug:
                print('three of a kind', self._is_three_of_kind()[1])
            return 40_000 + self._is_three_of_kind()[1] * 100 + self.cards[-1].rank()
        elif self._is_two_pairs()[0]:
            if debug:
                print('two pairs', self._is_two_pairs()[1])
            return 30_000 + self._is_two_pairs()[1] * 100 + self.cards[-1].rank()
        elif self._is_one_pair()[0]:
            if debug:
                print('one pair', self._is_one_pair()[1], self.cards[-1].rank())
            return 20_000 + self._is_one_pair()[1] * 100 + self.cards[-1].rank()
        else:
            if debug:
                print('nothing', self.cards[-1].rank())
            return self.cards[-1].rank()


hand1 = Hand('2H 2D 4C 4D 4S'.split())
hand2 = Hand('3C 3D 3S 9S 9D'.split())
if hand1.rank() > hand2.rank():
    print('Player 1 wins')
else:
    print('Player 2 wins')

