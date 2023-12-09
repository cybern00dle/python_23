"""
Queue entity
"""

from typing import Any, Iterable, Union


class CapacityOverflowError(Exception):
    """
    Is raised if a queue has reached its capacity.
    """


class InvalidElementTypeError(Exception):
    """
    Is raised when certain elements of an iterable instance do not match given criteria.
    """


class Queue:

    """
    A data structure working according to FIFO principle.
    """

    def __init__(self, storage: tuple = (), capacity: Union[int, None] = None):
        self.storage = list(storage)
        self._capacity = capacity

    def full(self) -> bool:
        """
        Checks if the queue has reached its capacity.
        :return: True if the queue is full, False otherwise
        """
        return True if (self._capacity and len(self.storage) == self._capacity) else False

    def put(self, elem: Any) -> None:
        """
        Adds an element to the end of the queue.
        :param elem: an element that needs to be added to the queue
        :return: None
        """
        if self.full():
            raise CapacityOverflowError('a queue has reached its capacity.')
        else:
            self.storage.append(elem)

    def get(self) -> Union[Any, None]:
        """
        Takes the first element out of the queue and returns it.
        :return: first element of the queue (None if the queue is empty)
        """
        return self.storage.pop(0) if self.storage else None

    def size(self) -> int:
        """
        Returns the number of elements in the queue aka its length.
        :return: length of the queue
        """
        return len(self.storage)

    def top(self) -> Union[Any, None]:
        """
        Returns the first element without taking it out of the queue.
        :return: first element of the queue (None if the queue is empty)
        """
        return self.storage[0] if self.storage else None

    def empty(self) -> bool:
        """
        Checks if the queue has any elements in it.
        :return: True if the queue is empty, False otherwise
        """
        return True if not self.storage else False

    # Task 1
    def get_until_even(self) -> None:
        """
        Extracts elements from a queue until its first element becomes an even number.
        Works for all-integer queues only.
        :return: None
        """
        if not all(isinstance(elem, int) for elem in self.storage):
            raise InvalidElementTypeError('not all elements are integers.')
        if self.empty():
            return None
        while self.top() % 2 != 0:
            self.get()


# Task 2
def sort_even_and_odd(sort: Iterable) -> Union[tuple[list, ...], None]:
    """
    Distributes all-integer iterable's elements between two queues,
    each receiving only odd and only even numbers, respectively.
    :param sort: an iterable instance which needs sorting
    :return: a tuple with queues' storages (first odd, then even),
    None in case of an empty iterable
    """
    if not all(isinstance(elem, int) for elem in sort):
        raise InvalidElementTypeError('not all elements are integers.')
    if not sort:
        return None
    queue_odd, queue_even = Queue(()), Queue(())
    for elem in sort:
        if elem % 2 == 0:
            queue_even.put(elem)
        else:
            queue_odd.put(elem)
    return queue_odd.storage, queue_even.storage


if __name__ == '__main__':

    q1 = Queue((1, 3, 5, 7, 9, 2, 4))
    q1.get_until_even()
    print(q1.storage)
    q2 = Queue()
    q2.get_until_even()
    print(q2.storage)
    # q3 = Queue((1, 3, 'Queue'))
    # q3.get_until_even()

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sort_even_and_odd(list1))
    list2 = []
    print(sort_even_and_odd(list2))
    # list3 = [1, 2, 3, 4, 'queue', 4.5]
    # print(sort_even_and_odd(list3))
