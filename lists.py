"""
What are linked lists?

    Sequential list of nodes that contain data, and hold references to other
    nodes containing data.

    Great for modelling trajectories, circular elements (polygons) etc.

    Used in implementations for Queue, Stack and List ADTs. Often used in
    implementations of adjacency lists for graphs.

    During implementations every node has a reference to the head and tail
    nodes to make easy additions and removals.

    Doubly linked lists not only contain pointers to the next node the sequence
    (singly linked lists) but also contain pointers to the previous node, allowing
    for traversal forwards and backwards.

Terminology:

    * Head: The first node in the linked list
    * Tail: The last node in the linked list
    * Pointer: Reference to another node
    * Node: Object containing data and pointer(s)

Complexity Analysis:

                    SLL     DLL
    ----------------------------
    Search          O(n)    O(n)
    Head Insert     O(1)    O(1)
    Tail Insert     O(1)    O(1)
    Head Remove     O(1)    O(1)
    Remove tail     O(n)    O(1)
    Remove i        O(n)    O(n)

Singly Linked List tail removal is O(n) because you cannot reset the tail pointer
after you have removed it once; and will need to traverse the list to the end (n)
to find the new tail.
"""
from typing import Any, Optional


class Node:
    """
    Node class to embed within the Linked List. Can hold any type of data.
    """

    def __init__(self, data: Any, prev: Optional["Node"], next: Optional["Node"]):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    """
    Doubly Linked List implementation in Python.
    """

    def __init__(self):
        self._size = 0
        self._head: Optional["Node"] = None
        self._tail: Optional["Node"] = None

    # region magic methods
    def __len__(self):
        return self._size

    def __str__(self):
        out = []
        trav = self._head
        while trav is not None:
            out.append(str(trav))
            trav = trav.next
        return str(out)

    # endregion

    # region public api

    def is_empty(self) -> bool:
        return self._size == 0

    def clear(self):
        trav = self._head

        while trav is not None:
            next_node = trav.next
            trav.prev = trav.next = None
            trav = next_node

        self._head = self._tail = None
        self._size = 0

    def prepend(self, data: Any):
        if self.is_empty():
            self._head = self._tail = Node(data=data, prev=None, next=None)
        else:
            self._head.prev = Node(data=data, prev=None, next=self._head)
            self._head = self._head.prev
        self._size += 1

    def append(self, data: Any):
        if self.is_empty():
            self._head = self._tail = Node(data=data, prev=None, next=None)
        else:
            self._tail.next = Node(data=data, prev=self._tail, next=None)
            self._tail = self._tail.next
        self._size += 1

    def first(self) -> Any:
        if self.is_empty():
            raise IndexError("Empty List")
        return self._head.data

    def last(self) -> Any:
        if self.is_empty():
            raise IndexError("Empty List")
        return self._tail.data

    def remove_first(self) -> Any:
        if self.is_empty():
            raise IndexError("Empty List")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1

        # clean up the pointers
        if self.is_empty():
            self._tail = None
        else:
            self._head.prev = None
        return data

    def remove_last(self) -> Any:
        if self.is_empty():
            raise IndexError("Empty List")
        data = self._tail.data
        self._tail = self._tail.prev
        self._size -= 1

        # clean up the pointers
        if self.is_empty():
            self._head = None
        else:
            self._tail.next = None
        return data

    def _remove_node(self, n: "Node"):
        # check if head or tail
        if n.prev is None:
            return self.remove_first()
        if n.next is None:
            return self.remove_last()

        # continue
        prev_node, next_node = n.prev, n.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self._size -= 1
        data = n.data

        # clean up memory
        n = None

        return data

    def remove(self, idx: int) -> Any:
        assert 0 <= idx < self._size, "OutOfBoundsError"
        # check head and tail removal
        if idx == 0:
            return self.remove_first()
        if idx == self._size - 1:
            return self.remove_last()

        trav = self._head
        for i in range(self._size):
            if i == idx:
                break
            trav = trav.next
        return self._remove_node(trav)

    # endregion


if __name__ == "__main__":
    dll = DoublyLinkedList()

    for i in range(20):
        dll.append(i)

    print(dll)
    dll.clear()
    print(dll)

    for i in range(20):
        dll.append(i)

    # remove an element
    dll.remove(7)
    print(dll)

    dll.prepend("HELLOWORLD")
    print(dll)

    dll.remove(len(dll) - 1)
    print(dll)

    dll.clear()
    print(dll)
