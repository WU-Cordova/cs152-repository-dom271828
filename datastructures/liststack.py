import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList, T

class ListStack(IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        self.data_type = data_type
        self.elements = LinkedList(data_type)
        self.count = 0
        # raise NotImplementedError("ListStack.__init__ is not implemented.")

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        self.elements.append(item=item)
        self.count += 1
        # raise NotImplementedError("ListStack.push is not implemented.")

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        raise NotImplementedError("ListStack.pop is not implemented.")

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        return self.elements.front

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.elements.empty
    
    def clear(self):
        """
        Clears all items from the stack.
        """
        self.elements.clear()
        self.count = 0

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        return item in self.elements
    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if not isinstance(other, ListStack):
            return False
        
        return self.elements == other.elements
        # raise NotImplementedError("ListStack.__eq__ is not implemented.")

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return self.count
    
    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str(self.elements)
        # raise NotImplementedError("ListStack.__str__ is not implemented.")

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        return repr(self.elements)
        # raise NotImplementedError("ListStack.__repr__ is not implemented.")
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
