class Card:
    suit_names=['Club','Diamonds','Hearts','Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
    
    def __lt__(self, other):
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        return self.rank < other.rank
    
card1 = Card(2, 11)
print(card1)


import random
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def __lt__(self):
        return self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_card(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def deal_hands(self,no_of_hands,no_of_card_per_hand):
        if no_of_hands*no_of_card_per_hand>len(self.cards):
            return "Not enough cards"
        hands=[]
        for i in range(no_of_hands):
            hand=Hand()
            for j in range(no_of_card_per_hand):
                card=self.deal_card()
                if card:
                    hand.add_card(card)
            hands.append(hand)
        return hands



    
deck = Deck()
print(deck)



class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label
hand=Hand('new hand')
print(hand.cards)
print(hand.label)
deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)


hands=deck.deal_hands(10,10)
for i,hand in enumerate(hands):
    print(f"Hand {i+1} : {hand}")







