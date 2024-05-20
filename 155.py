class MinStack:

    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.len += 1

    def pop(self) -> None:
        self.stack.pop()
        self.len -= 1

    def top(self) -> int:
        return self.stack[self.len - 1]

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()