from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
import random
import copy

class MultiDeck:

    def __init__(self):
        one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]
        multi_deck_list = [card for _ in range(random.choice([2, 4, 6, 8])) for card in copy.deepcopy(one_deck_list)]
        self._deck = multi_deck_list

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
    pass

if __name__ == '__main__':
    main()