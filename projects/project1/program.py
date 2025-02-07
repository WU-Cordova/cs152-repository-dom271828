# from datastructures.bag import Bag
from card import Card, CardSuit, CardFace

class MultiDeck:
    pass

class Game:
    def __init__(self, deck:MultiDeck):
        self.__deck = deck
    
    def run():
        pass
    
    pass

def main():
    
    card_suits = [suit.value for suit in list(CardSuit)]

    cards = []

    for suit in list(CardSuit):
        for face in list(CardFace):
            cards.append(Card(face.value, suit.value))

    for card in cards:
        print(card)



if __name__ == '__main__':
    main()
