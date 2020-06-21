from collections import deque


class Stack:
    def __init__(self):
        """Initiate our stack."""
        # the most used action in this app will be push() and pop()
        # so deque() will be the best choice
        self.stack = deque()

    def __repr__(self):
        return f'Stack({self.dump()!r})'

    def clear(self):
        """Clear stack."""
        self.stack.clear()

    def pop(self):
        """Pop top item from the stack."""
        if not self.size():
            return None
        return self.stack.pop()

    def push(self, item):
        """Add item to the top of the stack."""
        self.stack.append(item)

    def size(self):
        """Return size of the stack."""
        return len(self.stack)

    def peek(self, n=1):
        """Look at n items on top of the stack."""
        if self.size() >= n:
            return list(self.stack)[-n:]
        else:
            return []

    def dump(self):
        """Look at entire stack."""
        return list(self.stack)

    def dup(self, n=1):
        """Diplicated n items on top of the stack and adds it to the stack."""
        if self.size() >= n:
            self.stack += deque(self.peek(n))

    def depth(self):
        """Add the size of the stack to the top of the stack."""
        self.push(self.size())

    def drop(self, n=1):
        """Drop n items from the top of the stack."""
        if self.size() >= n:
            if n == 1:
                self.pop()
            else:
                self.stack = deque(list(self.stack)[:-n])

    def roll(self, n=1):
        """Rotate stack n elements forwards."""
        self.state.rotate(n)

    def rolld(self, n=1):
        """Rotate stack n elements backwards."""
        self.roll(-n)

    def swap(self):
        """Swap 2 top items on top of the stack."""
        if self.size() >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def pick(self, n=1):
        """Pop the nth item from the stack and append it to the stack."""
        if self.size() >= n:
            stack = list(self.stack)
            item = stack.pop(-n)
            stack.append(item)
            self.stack = deque(stack)


stack = Stack()
