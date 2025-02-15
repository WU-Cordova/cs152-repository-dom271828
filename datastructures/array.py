# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy

from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: # by Friday: __init__ implemented & sunny day cases of get/setters
        self.__logical_size = len(starting_sequence)
        self.__capacity = self.__logical_size # physical size
        self.__datatype = data_type
        
        self.__elements = np.empty(self.__logical_size, dtype = self.__datatype) # creates an empty array with logical size as size and datatype as dtype

        for i in range(self.__logical_size):
            self.__elements[i] = copy.deepcopy(starting_sequence[i]) 

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            start: int = slice.start
            stop: int = slice.stop
            step: int = slice.step

            # check if start/stop are inbounds; if not raise exception
            return Array(starting_sequence=self.__elements[start:stop:step].tolist, data_type=self.__datatype)
        
        elif isinstance(index, int):
            # same check: see if index is out of bounds & if so raise exception
            return self.__elements[index] # item if index is int
    
        # raise NotImplementedError('Indexing not implemented.')
    
    def __setitem__(self, index: int, item: T) -> None:
        if index in range(self.__elements) and type(item) == self.__datatype:
            self.__elements[index] = item
        elif index not in range(self.__elements):
            raise ValueError("Index is out of bounds")
        elif type(item != self.__datatype):
            raise TypeError("item does not match datatype")
        # raise NotImplementedError('Indexing not implemented.')

    def append(self, data: T) -> None:
        raise NotImplementedError('Append not implemented.')

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int:
        return self.__logical_size
        raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        raise

    def __delitem__(self, index: int) -> None:
        raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        return item in self.__elements 
        # raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        self.__logical_size = 0
        self.__capacity = 0
        self.__elements = np.empty(self.__logical_size, dtype = self.__datatype)
        # raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')