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


class DLL:
    """
    Doubly Linked List implementation in Python.
    """
    pass
