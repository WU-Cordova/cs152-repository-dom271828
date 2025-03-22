import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self._top = 0 
        self._maxsize = max_size
        self._data_type = data_type
        self.stack = Array(starting_sequence=[data_type() for _ in range(max_size)], data_type=data_type)
        # raise NotImplementedError('ArrayStack is not implemented')

    def push(self, item: T) -> None:
        if self.full == True:
            raise(IndexError("Stack is full brotha"))
        self.stack[self._top] = item
        self._top += 1
        # raise NotImplementedError

    def pop(self) -> T:
       
       if self._top < 1:
            raise(IndexError)
       
       top = self.stack[self._top - 1]
       self.stack[self._top] = self._data_type()
       self._top -= 1
       return top
       # raise NotImplementedError

    def clear(self) -> None:
       self._top = 0
       self.stack = Array(starting_sequence=[self._data_type() for _ in range(self._maxsize)], data_type=self._data_type)
       # raise NotImplementedError
    @property
    def peek(self) -> T:
        return self.stack[self._top - 1]
       # raise NotImplementedError

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self._maxsize
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        print(self._top)
        return self._top - 1 == self._maxsize
        # raise NotImplementedError

    @property
    def empty(self) -> bool:
        return self._top == 0 
        # raise NotImplementedError
    def __eq__(self, other: object) -> bool:
       if not isinstance(other, ArrayStack):
            print("triggered statement 1")
            return False
       if other._top != self._top:
            print("triggered statement 2")
            return False
       for index in range(self.maxsize):
           if self.stack[index] != other.stack[index]:
               return False
       # for i in r
       # raise NotImplementedError
       return True

    def __len__(self) -> int:
       return self._top

       # raise NotImplementedError
    
    def __contains__(self, item: T) -> bool:
       return item in self.stack
    
    def __str__(self) -> str:
        return str([int(self.stack[i]) for i in range(self._top)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self._maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

