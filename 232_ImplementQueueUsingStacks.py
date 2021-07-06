class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp, self.stack = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.temp.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack:
            while self.temp:
                self.stack.append(self.temp.pop())
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return bool(not self.temp and not self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
