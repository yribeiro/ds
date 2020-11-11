"""

What is a stack?

    One ended linear data structure that models a real world stack.
    The stack contains two operations push and pop, which put things
    on top of the stack (push) and take things off the top (pop).

    This behaviour is LIFO. Last In First Out behaviour.

    Stacks are used pretty much everywhere.
        * Undo in text editors
        * Navigate backwards and forwards in browsers
        * Compilers for matching brackets and braces
        * Models piles of things
        * Can be used in Depth First Search (DFS)

Complexity Analysis (Implemented using a linked list):

                Complexity
    ----------------------------
    Pushing         O(1)
    Popping         O(1)
    Peeking         O(1)
    Searching       O(n)
    Size            O(1)

"""

from lists import DoublyLinkedList


class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)

    def is_empty(self) -> bool:
        return self.storage.is_empty()

    def push(self, data):
        self.storage.append(data)

    def pop(self):
        data = self.storage.remove_last()
        return data

    def peek(self):
        return self.storage.last()


if __name__ == "__main__":
    """
    Given a string made up of brackets: ()[]{}
    determine whether brackets are properly matched
    
    Test Cases:
        [{}] -> True
        (()()) -> True
        {] -> False
        [()]))() -> False
        []{}({}) -> True
    """


    def bracket_match(inp_str: str) -> bool:
        _stack = Stack()
        brackets = {")": "(", "}": "{", "]": "["}
        for char in inp_str:
            if not _stack.is_empty() and char in brackets.keys():
                if _stack.peek() == brackets[char]:
                    _stack.pop()
                else:
                    _stack.push(char)
            else:
                _stack.push(char)
        return _stack.is_empty()


    cases = ["[{}]", "(()())", "{]", "[()]))()", "[]{}({})"]
    expected = [True, True, False, False, True]
    results = []
    for case in cases:
        result = bracket_match(case)
        print(result)
        results.append(result)
    print(f"Expected: {expected}")
    print(f"Results: {results}")
