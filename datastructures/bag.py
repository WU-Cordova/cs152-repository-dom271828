from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag = { }
        if items is not None:
            for item in items:
                if item in self.__bag: # put in add function
                    self.__bag[item] += 1
                else:
                    self.__bag[item] = 1

    def add(self, item: T) -> None:
        if item in self.__bag: 
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1
        if item == None:
            raise TypeError("NoneType added")
        # raise NotImplementedError("add method not implemented")

    def remove(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] -= 1
        else:
            raise ValueError
        # raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        if item in self.__bag:
            return self.__bag[item]
        else:
            return 0

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")