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

    @property
    def heap_size(self):
        return len(self._heap)

    def is_empty(self) -> bool:
        return self.heap_size == 0

    def clear(self):
        self._heap = []
        self._hash = {}

    def poll(self) -> Any:
        return self._remove_at(0)

    def peek(self) -> Any:
        return copy(self._heap[0]) if not self.is_empty() else None

    def add(self, value: Any):
        # automatically adding the element to the end of the heap
        self._heap.append(value)

        # update the hashmap for easy lookups
        if self.contains(value):
            self._hash[value].add(self.heap_size - 1)
        else:
            self._hash[value] = {self.heap_size - 1}

        # now we need to satisfy the heap invariant and swim the value
        # up or down the list
        self._swim(self.heap_size - 1)

    def _swap(self, index_a: int, index_b: int):
        # update the map - items in heap are the keys
        self._hash[self._heap[index_a]].remove(index_a)
        self._hash[self._heap[index_a]].add(index_b)

        self._hash[self._heap[index_b]].remove(index_b)
        self._hash[self._heap[index_b]].add(index_a)

        # update the underlying heap
        temp = copy(self._heap[index_a])
        self._heap[index_a] = self._heap[index_b]
        self._heap[index_b] = temp

    def _swim(self, index: int):
        # this method is bubbling up
        parent = (index - 1) // 2
        # this loop keeps going while the index isn't the root node
        # and while the element at the index is <= it's parent
        while index > 0 and self._heap[index] <= self._heap[parent]:
            # swap the parent and the child
            self._swap(parent, index)
            index = parent
            # get the parent above the current parent index
            parent = (index - 1) // 2

    def _sink(self, index: int):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = left  # assume left is the smallest

            # sanity check for the right child
            if right < len(self._heap) and self._heap[right] <= self._heap[left]:
                smallest = right

            # scanning from left to right in the tree as we go down levels
            # so the left child will be the first to go out of bounds

            # break the loop if the left is OOB or the child node is no longer
            # greater than the current index
            if left >= self.heap_size or self._heap[index] <= self._heap[smallest]:
                break

            # move the value at the current index into the index
            # of the smallest child
            self._swap(smallest, index)
            index = smallest

    def _remove_at(self, index: int) -> Any:

        if self.heap_size == 1:
            item = self._heap[index]
            # remove the end item in the heap
            self._heap.pop(-1)
            # update the hash map - i.e. remove the index where the item was held
            self._hash[item].pop()
        else:
            item = self._heap[index]

            # swap the item with the end in the list
            self._swap(index, self.heap_size - 1)

            # remove the end item in the heap
            self._heap.pop(-1)
            # update the hash map - i.e. remove the index where the item was held
            self._hash[item].pop()

            # get the new element at index
            elem = self._heap[index]

            # try sinking
            self._sink(index)

            # try swimming if sinking doesn't move the element
            if self._heap[index] == elem:
                self._swim(index)

        return item

    def remove(self, value: Any) -> Any:
        if self.contains(value):
            idx_set = self._hash[value]
            # provide the first element of the set
            item = self._remove_at(next(iter(idx_set)))
            return item
        else:
            raise ValueError(f"PriorityQueue does not contain element: {value}")

    def contains(self, value: Any) -> bool:
        # In Python 3.x the in operation on the dict_keys object is O(1)
        # without a hash map we would need to scan the list with O(n) worst case
        return True if value in self._hash.keys() else False


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.add(23)
    pq.add(5)
    pq.add(40)
    pq.add(-2)
    pq.add(0)

    for i in range(pq.heap_size):
        print(pq.poll())
