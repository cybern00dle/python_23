"""
Stack entity
"""
import typing


class OutOfLimitError(Exception):
    """
    Is raised if a stack is out of limit.
    """


class Stack:
    """
    Creates a stack entity.
    """

    def __init__(self, storage=(), limit=None):
        self.storage = list(storage)
        self._limit = limit

    def check_limit(self) -> bool:
        return True if (self._limit and len(self.storage) == self._limit[0]) else False

    def empty(self) -> bool:
        return True if not self.storage else False

    def push(self, arg: typing.Any) -> None:
        if self.check_limit():
            raise OutOfLimitError('stack is out of limit')
        self.storage.append(arg)

    def pop(self) -> typing.Any:
        return self.storage.pop() if self.storage else None

    def top(self) -> typing.Any:
        return self.storage[-1] if self.storage else None

    def size(self) -> int:
        return len(self.storage)

    def clear(self) -> None:
        self.storage.clear()


def check_brackets(string: str) -> bool:
    stack = Stack()
    brackets = {']': '[', '}': '{', ')': '('}
    for i in string:
        if i in ']})':
            top = stack.top()
            if top == brackets[i]:
                stack.pop()
            else:
                return False
        else:
            stack.push(i)
    return True


str_test_list = ['({[][]()})', '()', '([({})])', '([({})](){})', '([({})][]])', '({[})']
for str_test in str_test_list:
    print(check_brackets(str_test))


def sort_stack(stack: Stack):
    tmp_stack = []
    while not stack.empty():
        element = stack.pop()
        while tmp_stack and tmp_stack[-1] > element:
            stack.push(tmp_stack.pop())
        tmp_stack.append(element)
    return tmp_stack


stack1 = Stack([1, 5, 6, 2, 8])
print(sort_stack(stack1))
