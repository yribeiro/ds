"""

What is a Priority Queue?

    Priority Queue is an ADT that operates the same as a normal Queue, except
    that elements have a certain priority associated with them. The priority determines
    the order in which the elements are removed from the queue.

    PQs are used in:
        * In Dijkstra's shortest path algorithm
        * Anytime you need to fetch the next best or next worst element
        * Used in Huffman coding which is used for lossless data compression
        * Best First Search (BFS) algorithms such as A*
        * Minimum Spanning Tree (MST) algorithms

What is a Heap?

    A heap is a tree based data structure that satisfies the heap invariant
    property:

        "If A is a parent node of B then A is ordered with respect to B for
         all nodes A, B in the heap."

    This just means that a parent node is either >= or <= than the value of
    of a child nodes for all nodes. This leads to two types of heaps: min and max heaps.

    Examples of a Max Heap:
                                         8
                                       /  \
                                      7    6
                                     / \  | \
                                    3  2  5  4

    Note: Binary heaps / trees are ones where the parent node exactly two child nodes.

    Heaps are the canonical way to implement Priority Queues as they are more efficient
    than lists.

Complexity Analysis (implemented as binary heap)

                                     Complexity
    ----------------------------------------------
    Binary Heap Construction            O(n)        # using heap sort to go from unordered to ordered
    Polling                           O(log(n))
    Peeking                             O(1)
    Add                               O(log(n))
    Naive Removing                      O(n)
    Advanced Removing (hash table)    O(log(n))
    Naive contains                      O(n)
    Advanced contains (hash table)      O(1)

    Adding a hash table increases space by O(n)

"""
from copy import copy
from typing import Any, Dict, List, Set


class PriorityQueue:
    """
    Priority Queue that allows any comparable items to be stored and retrieved by priority.
    """

    def __init__(self):
        # hash table to store the value -> positions map
        self._hash: Dict[Any, Set[int]] = {}
        # this is an array representation of a tree
        self._heap: List[Any] = []

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def clear(self):
        self._heap = []
        self._hash = {}

    def poll(self) -> Any:
        return self.remove_at(0)

    def peek(self) -> Any:
        return copy(self._heap[0]) if not self.is_empty() else None

    def add(self, value: Any):
        # automatically adding the element to the end of the heap
        self._heap.append(value)

        # update the hashmap for easy lookups
        if self.contains(value):
            self._hash[value].add(len(self._heap) - 1)
        else:
            self._hash[value] = {len(self._heap) - 1}

        # now we need to satisfy the heap invariant and swim the value
        # up or down the list
        self.swim(len(self._heap) - 1)

    def swim(self, index: int):
        raise NotImplemented()

    def sink(self, index: int):
        raise NotImplemented()

    def swap(self, index_a: int, index_b: int):
        raise NotImplemented()

    def remove_at(self, index: int) -> Any:
        raise NotImplemented()

    def remove(self, value: Any) -> Any:
        raise NotImplemented()

    def contains(self, value: Any) -> bool:
        # In Python 3.x the in operation on the dict_keys object is O(1)
        # without a hash map we would need to scan the list with O(n) worst case
        return True if value in self._hash.keys() else False
