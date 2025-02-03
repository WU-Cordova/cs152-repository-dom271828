from enum import Enum

class CardSuit(Enum):
    pass # i.e. HEARTS = "❤" 

class CardFace(Enum):
    pass # i.e. ONE = "1"

@dataclass
class Card:
    card_face: CardFace
    card_suit: CardSuit


