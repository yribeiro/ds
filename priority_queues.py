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


class PriorityQueue:
    pass
