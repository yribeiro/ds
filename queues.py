"""

What is a Queue?

    A linear data structure which models real world queues. Queues
    have two primary operations - enqueue and dequeue.

    Dequeue takes elements off the front of the queue. Enqueue puts
    elements into the back of the queue.

    Queues are used in many applications:
        * Used to model real world queues.
        * Used to efficiently keep track of the x most recent additions
        * Used to manage web server requests in a first come first server manner
        * Used in Breadth First Search algorithms

Complexity Analysis (Implemented using a linked list):

                Complexity
    ----------------------------
    Enqueue         O(1)
    Dequeue         O(1)
    Peeking         O(1)
    Searching       O(n)
    Removal         O(n)
    Is Empty        O(1)

"""
from typing import Any

from lists import DoublyLinkedList


class Queue:

    def __init__(self):
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)

    def is_empty(self) -> bool:
        return self.storage.is_empty()

    def enqueue(self, data: Any):
        self.storage.prepend(data)

    def dequeue(self) -> Any:
        return self.storage.remove_last()

    def peek(self) -> Any:
        return self.storage.last()


if __name__ == "__main__":
    queue = Queue()
    data = [chr(i) for i in range(10)]

    for d in data:
        queue.enqueue(d)
        print(queue)

    print("-" * 20)

    for _ in range(10):
        print(queue)
        _ = queue.dequeue()
