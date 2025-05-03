from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """ Initializes variables self.__bag and self.__count """
        self.__bag = { } # dictionary - key is the item, value is the item count
        self.__count = 0
        if items is not None:
            for item in items:
                if item in self.__bag:
                    self.__bag[item] += 1
                else:
                    self.__bag[item] = 1

    def add(self, item: T) -> None:
        """ Adds an item to the bag; item:1 if item is new and item:count + 1 if
        item is already in bag
        """
        if item in self.__bag: # Smaller effect if item is already in bag
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1 
        self.__count += 1
        if item == None:
            raise TypeError("Item cannot be None") # TypeError and a lil message if item added is None

    def remove(self, item: T) -> None:
        """ Removes item from bag, accomodating for invalid statements """
        if item in self.__bag: # subtracts one iteration of an item, as well as a value of its count
            self.__bag[item] -= 1
            self.__count -= 1 
        else:
            raise ValueError("item is not in bag") # ValueError and a lil message if item isn't valid to be removed

    def count(self, item: T) -> int:
        """ Returns value for key item in bag, equivalent to each instance
         of the item added to the bag """
        if item in self.__bag:
            return self.__bag[item]
        else:
            return 0 # returns 0 if item is not in bag

    def __len__(self) -> int:
        """ Returns count as added/reduced by add/remove """
        return self.__count # count increases/decreases depending on items that are added or removed

    def distinct_items(self) -> Iterable[T]:
        """ Returns iterable of self.__bag that contains unique values """
        return self.__bag # returns dictionary of unique values

    def __contains__(self, item) -> bool:
        """ Return bool if item is in self.__bag """
        return item in self.__bag # Returns either True or False if item is in the bag

    def clear(self) -> None:
        """ Clears bag, including length """
        self.__count = 0 # Makes it so __len__ function returns 0
        self.__bag = { } # Reverts bag to a blank dictionary