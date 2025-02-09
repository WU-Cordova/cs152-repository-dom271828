from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
import random
import copy

class MultiDeck:

    def __init__(self, decks: int):
        cards = []

        for _ in range(decks):
            for suit in list(CardSuit):
                for face in list(CardFace):
                    cards.append(Card(face.value, suit.value))
        random.shuffle(cards)

        self._cards = cards

    def draw(self):
        drawncard = self._cards.pop()
        return drawncard
    
    def reshuffle(self, num):
        self.__init__(num)

    pass

class Game:
    def __init__(self):
        self._playerhand = Bag()
        self._dealerhand = Bag()

    def run():
        pass
    
    pass


def main():
    one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]
    print(f"One deck has {len(one_deck_list)} cards")
    print("".join(str(card) for card in one_deck_list))

    deck_count = random.choice([2, 4, 6, 8])
    multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]

    print(f"{deck_count} decks have {len(multi_deck_list)} cards")
    print("".join(str(card) for card in multi_deck_list))

    deck_bag = Bag(*multi_deck_list)
    print(list(deck_bag.distinct_items()))
    two_cards = random.sample(list(deck_bag.distinct_items()), 2)
    print(f"Two cards: {"".join(str(card) for card in two_cards)} with a face value of: {sum(card.card_face.face_value() for card in two_cards)}")

if __name__ == '__main__':
    main()