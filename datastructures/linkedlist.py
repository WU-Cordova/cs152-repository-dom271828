from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list: LinkedList[T] = LinkedList(data_type=data_type)
        for item in sequence:
            linked_list.append(item)
        
        return linked_list

    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise(TypeError)
        new_node: LinkedList.Node = LinkedList.Node(data = item)
        if self.empty:
            self.head = self.tail = new_node
        else:
            old_tail = self.tail
            self.tail.next = self.tail = new_node
            new_node.previous = old_tail
        self.count += 1

    def prepend(self, item: T) -> None:
        # opposite of append
        if not isinstance(item, self.data_type):
            raise(TypeError)
        
        new_node: LinkedList.Node = LinkedList.Node(data = item)
        if self.empty:
            self.head = self.tail = new_node
        else:
            old_head = self.head
            self.head.previous = self.head = new_node 
            new_node.next = old_head
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        # Steps: Creates node with item
        # set prev.next to new node
        # set new_node.prev to target.prev
        # set new_node.next to target
        # set travel.previous to new_node (ts could use prepend)
        if not isinstance(item, self.data_type) or not isinstance(target, self.data_type):
            raise(TypeError)
        
        new_node: LinkedList.Node = LinkedList.Node(data = item)

        if self.head and self.head.data == target:
            self.prepend(item)
            return

        travel = self.head
        while travel is not None:

            if travel.data == target:
                break

            travel = travel.next
        
        if travel is None:
            raise(ValueError(f"ts target({target}) is not in the list"))
        
        travel.previous.next = new_node
        new_node.previous = travel.previous
        new_node.next = travel
        travel.previous = new_node
        self.count += 1
        # if travel is None:
            # raise ValueError(f"Target not in the linked list")
        # raise NotImplementedError("LinkedList.insert_before is not implemented")

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise(TypeError)
        
        new_node: LinkedList.Node = LinkedList.Node(data = item)

        if self.tail and self.tail.data == target:
            self.append(item)
            return

        travel = self.head
        while travel is not None:

            if travel.data == target:
                break

            travel = travel.next
        
        if travel is None:
            raise(ValueError(f"ts target({target}) is not in the list"))
        
        travel.next.previous = new_node
        new_node.next = travel.next
        new_node.previous = travel
        travel.next = new_node
        self.count += 1
        # raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise(TypeError)
        
        if self.head and self.head.data == item:
            self.pop()
            return

        travel = self.head
        while travel is not None:

            if travel.data == item:
                break

            travel = travel.next
        
        if travel is None:
            raise(ValueError(f"ts target({item}) is not in the list"))
        
        travel.previous.next = travel.next
        travel.next.previous = travel.previous
        travel = None
        return
    
    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise(TypeError)
        
        if self.head and self.head.data == item:
            self.pop_front()
            return

        travel = self.head
        while travel is not None:
            if travel.data == item:

                if travel == self.tail:
                    self.tail = travel.previous
                    self.tail.next = None
                    self.count -= 1
                    return
                
                self.count -= 1
                travel.previous.next = travel.next
                travel.next.previous = travel.previous

            travel = travel.next
        
        if self.tail.data == item:
            self.pop()
        
        if travel is None:
            raise(ValueError(f"ts target({item}) is not in the list"))


    def pop(self) -> T:
        if not self.empty:
            data = self.tail.data
            self.tail.previous = self.tail
            self.tail.next = None
            self.count -= 1
            return data
        else:
            raise(IndexError("Ts list is empty"))

    def pop_front(self) -> T:
        if not self.empty:
            data = self.head.data
            self.head.previous = self.head
            self.head.previous = None
            self.count -= 1
            return data
        else:
            raise(IndexError("Ts list is empty"))
        
    @property
    def front(self) -> T:
        if not self.head:
            raise(IndexError("ts list is empty"))
        return self.head.data
        
    @property
    def back(self) -> T:
        if not self.tail:
            raise(IndexError("ts list is empty"))
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.count = 0
        self.head = None
        self.tail = None

    def __contains__(self, item: T) -> bool:
        for i in self:
            if i == item:
                return True
        return False
    
    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        reversed_list = LinkedList(data_type=self.data_type)
        reverse_travel = self.tail

        while reverse_travel is not None:
            reversed_list.append(reverse_travel.data)
            reverse_travel = reverse_travel.previous
        
        return reversed_list

    
    def __eq__(self, other: object) -> bool:
        
        if not isinstance(other, LinkedList):
            return False
        
        if self.count != other.count:
            return False

        self_travel = self.head
        other_travel = other.head

        while self_travel and other_travel:
            if self_travel.data != other_travel.data:
                return False
            self_travel = self_travel.next
            other_travel = other_travel.next

        return True
        

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
            print(items)
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
