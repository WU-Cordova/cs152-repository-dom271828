from dataclasses import dataclass
from enum import Enum

class CardSuit(Enum):
    HEARTS = "❤" 
    CLUBS = "♣"
    SPADES = "♠️"
    DIAMONDS = "♦"

class CardFace(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "10"
    QUEEN = "10"
    KING = "10"
    ACE = ["1","11"]

@dataclass
class Card:
    card_face: CardFace
    card_suit: CardSuit

class MultiDeck:
    pass

class Game:
    pass