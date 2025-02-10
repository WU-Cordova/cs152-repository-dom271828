from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace
import random
import copy

DEBUG = True
class MultiDeck:

    def __init__(self):
        one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]
        deck_count = random.choice([2, 4, 6, 8])
        DEBUG and print(f"This deck consists of {deck_count} decks")
        multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]
        random.shuffle(multi_deck_list)
        self._deck = multi_deck_list

    def __repr__(self) -> str:
        return f"Deck consists of: {"".join(str(card) for card in self._deck)}"
    
    # def shuffle(self):
        # random.shuffle(self._deck) 

class Game:
    def __init__(self):
        self.__playerhand: list[Card] = []
        self.__dealerhand: list[Card] = []

    def drawtohand(self, deck:Bag, hand:list[Card], score:int):
        """ Transfers a random card from deck (Bag) to hand (Bag)
        Return: Card Value """
        card:Card = random.choice(list(deck.distinct_items()))
        hand.append(card)
        deck.remove(card)
        value = card.card_face.face_value()
        if value == 11 and score > 11: # Special Case: If score will bust when Ace is played at the wrong time
            return 1
        return value

    def run(self):
        finished = False

        while finished != True:

            finishround: bool = False
            bust: bool = False
            blackjack: bool = False
            cards = MultiDeck()
            deck_bag = Bag(*cards._deck)
            pscore: int = 0
            dscore: int = 0
            turn: int = 0
        

            while finishround != True:
                if turn == 0:

                    for _ in range(2):
                        pscore += self.drawtohand(deck_bag, self.__playerhand, pscore)
                        dscore += self.drawtohand(deck_bag, self.__dealerhand, dscore)
                    
                
                    print(f"Player's Hand Is: {"".join(str(card) for card in self.__playerhand)} | Score: {pscore}")
                    match dscore:
                        case 21:
                            print(f"Dealer's Hand Is: {"".join(str(card) for card in self.__dealerhand)} | Score: {dscore}")
                        case _:
                            print(f"Dealer's Hand Is: {"".join(str(self.__dealerhand[0]))} [Hidden] | Score: {self.__dealerhand[0].card_face.face_value()}")
                    print()

                    if dscore == 21 or pscore == 21:
                        turn += 1
                        blackjack = True
                        finishround == True
                
                if turn % 2 == 0:
                    print(f"Player's Hand Is: {"".join(str(card) for card in self.__playerhand)} | Score: {pscore}")
                    response = input("Would you like to (H)it or (S)tay? ").strip().upper()
                    if response == "H":
                        pscore += self.drawtohand(deck_bag, self.__playerhand, pscore)
                        print()
                        print(f"Player's Hand Is: {"".join(str(card) for card in self.__playerhand)} | Score: {pscore}")
                        if pscore > 21:
                            bust = True
                            print("Bust! You went over 21 points")
                        turn += 1
                    if response == "S":
                        turn += 1
                else:
                    while dscore < 17:
                        dscore += self.drawtohand(deck_bag, self.__dealerhand, dscore)
                    print()
                    if dscore != 21:
                        print(f"Dealer's Hand Is: {"".join(str(card) for card in self.__dealerhand)} | Score: {dscore}")
                    finishround = True
                    if dscore > 21 or pscore > 21:
                        bust = True
            
            if pscore > 0 and dscore > 0:
                if pscore > 21:
                    print("Player bust! Dealer Wins!")
                elif dscore > 21:
                    print("Dealer bust! Player Wins!")
                elif pscore == 21 and blackjack == True:
                    print("Blackjack! Player Wins!")
                elif dscore == 21 and blackjack == True:
                    print("Blackjack! Dealer Wins!")
                elif pscore > dscore and bust != True:
                    print("Player Wins!")
                elif dscore > pscore and bust != True:
                    print("Dealer Wins!")
                elif pscore == dscore:
                    print("Tie!")
                print()
            
            gameover = input("Would you like to play again? (Y)es or (N)o ").strip().upper()
            if gameover == "Y":
                self.__playerhand.clear()
                self.__dealerhand.clear()
                finishround = False
            elif gameover == "N":
                finished = True

        print("Thanks for playing!") 


def main():
    BagJack = Game()
    BagJack.run()


if __name__ == '__main__':
    main()