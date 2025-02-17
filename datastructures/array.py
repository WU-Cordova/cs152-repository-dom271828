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
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting sequence is not a sequence")
        
        self.__logical_size = len(starting_sequence)
        self.__capacity = self.__logical_size # physical size
        self.__datatype = data_type
        
        for i in starting_sequence:
            if type(i) != data_type:
                raise TypeError
            
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
        
        elif not isinstance(index, int) or isinstance(index, slice):
            raise TypeError("Ts index is neither a slice or index")
    
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
        print("size pre-append is", self.__logical_size)
        self.__logical_size += 1
        self.__elements[self.__logical_size - 2] = data
        print(self.__logical_size)
        return None
        # raise NotImplementedError('Append not implemented.')

    def append_front(self, data: T) -> None:
        print("size pre-append is", self.__logical_size)
        self.__logical_size += 1
        self.__elements[0] = data
        print(self.__logical_size)
        return None
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        for i in range(self.__logical_size - 1):
            self.__elements[i] = self.__elements[i + 1]
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        for i in range(0, self.__logical_size - 1):
            self.__elements[i] = self.__elements[i + 1]
        self.__logical_size -= 1
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int:
        return self.__logical_size
        # raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        if self.__elements == other.__elements and self.__logical_size == other.__logical_size:
            return True
        else:
            return False
        # raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        for i in range(self.__logical_size):
            yield self.__elements[i]

    def __reversed__(self) -> Iterator[T]:
        return True

    def __delitem__(self, index: int) -> None:
        for i in range(index, self.__logical_size - 1):
            self.__elements[i] = self.__elements[i + 1]
        self.__logical_size -= 1

    def __contains__(self, item: Any) -> bool:
        return item in self.__elements 
        # raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        self.__logical_size = 0
        self.__capacity = 0
        self.__elements = np.empty(0, dtype = self.__datatype)
        # raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self.__elements) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {self.__capacity}, type: {self.__datatype}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')