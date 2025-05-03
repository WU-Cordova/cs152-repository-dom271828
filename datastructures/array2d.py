from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.__row_index = row_index
            self.__array = array
            self.__num_columns = num_columns

        def map_index(self, row_index: int, col_index) -> int:
            return row_index * self.__num_columns + col_index
        
        def __getitem__(self, column_index: int) -> T:
            if column_index > self.__num_columns - 1:
                raise(IndexError)
            index: int = self.map_index(self.__row_index, column_index)
            return self.__array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index: int = self.map_index(self.__row_index, column_index)
            self.__array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            for i in range(self.__num_columns):
                yield self[i]
        
        def __reversed__(self) -> Iterator[T]:
            for i in range(self.__num_columns - 1, -1, -1):
                yield self[i]

        def __len__(self) -> int:
            return self.__num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.__num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.__num_columns - 1)])}, {str(self[self.__num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("must be a sequence of sequences")
        else:
            for _ in starting_sequence:
                if isinstance(_, str) or not isinstance(_, Sequence):
                    raise ValueError("must be a sequence of sequences")
        
        self.__data_type = type(starting_sequence[0]) if data_type == object else data_type
        self.__rows_len = len(starting_sequence)
        self.__cols_len = len(starting_sequence[0])

        for list in starting_sequence:
            if len(list) != self.__cols_len:
                raise ValueError("must be a sequence of sequences with the same length")
            for i in list:
                if type(i) != self.__data_type:
                    raise ValueError("All items must be of the same type")
        
        py_list = []
        for row in range(self.__rows_len):
            for col in range(self.__cols_len):
                py_list.append(starting_sequence[row][col])

        self.__elements2d = Array(starting_sequence=py_list, data_type=data_type)
        

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        sequence2d = [[data_type() for _ in range(cols)] for _ in range(rows)]
        # return Array2d for this
        return Array2D(starting_sequence=sequence2d, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index > self.__rows_len - 1:
            raise(IndexError)
        return self.Row(row_index=row_index, array=self.__elements2d, num_columns=self.__cols_len)    
    
    def __iter__(self) -> Iterator[Sequence[T]]:
        for row in range(self.__rows_len):
            yield self[row]
        # raise NotImplementedError('Array2D.__iter__ not implemented.')
    
    def __reversed__(self):
        for row in range(self.__rows_len - 1, -1, -1):
            yield self[row]
    
    def __len__(self):
        return self.__rows_len
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array2D):
            return False

        if self.__rows_len != other.__rows_len or self.__cols_len != other.__cols_len:
            return False

        for row in range(self.__rows_len):
            for col in range(self.__cols_len):
                if self[row][col] != other[row][col]:
                    return False

        return True
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__rows_len} Rows x {self.__cols_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    empty3x3 = Array2D.empty(rows=3, cols=3, data_type=int)
    empty3x3 == Array2D.empty(rows=3, cols=3, data_type=int)
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')