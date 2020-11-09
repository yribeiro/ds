class DynamicArray:
    """
    Implementation of a DynamicArray using inbuilt python types. Implementation is to drive the point home.

    Dynamic Arrays can be made out of static arrays:

    Lookup at idx: O(1)
    Insertion at idx: O(1)
    Appending: O(n)
    Removal: O(n)
    """

    def __init__(self, capacity=5):
        self.__capacity = capacity
        self.__length = 0
        # fill with placeholder values
        self.__array = [None for _ in range(self.__capacity)]

    def __len__(self):
        return self.__length

    def __str__(self):
        return str(self.__array)

    # define api methods for Dynamics Arrays
    def is_empty(self) -> bool:
        return self.__len__() == 0

    def get(self, index):
        return self.__array[index]

    def set(self, index, value):
        self.__array[index] = value

    def clear(self):
        self.__array = [None for _ in range(self.__capacity)]
        self.__length = 0

    def add(self, value):
        # deal with capacity being over
        if self.__length + 1 >= self.__capacity:
            self.__capacity = self.__capacity * 2 if self.__capacity != 0 else 1
            new_arr = [None for _ in range(self.__capacity)]
            for idx, elem in enumerate(self.__array):
                new_arr[idx] = elem
            self.__array = new_arr

        self.__array[self.__length] = value
        self.__length += 1

    def remove_at(self, index):
        if index > self.__length:
            raise IndexError("Out of bounds")
        data = self.__array[index]
        self.__array = [self.__array[idx] for idx in range(self.__capacity) if idx != index]
        self.__length -= 1
        return data

    def remove(self, elem):
        result = False
        for idx in range(self.__length):
            if self.__array[idx] == elem:
                self.remove_at(idx)
                result = True
                break
        return result


if __name__ == "__main__":
    numbers = DynamicArray()
    for i in range(20):
        numbers.add(i)

    print(numbers.remove(15))
    print(f"Numbers: {numbers} with length: {len(numbers)}")
