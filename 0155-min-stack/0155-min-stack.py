class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stackmin:
            val = min(val, self.stackmin[-1])
        else:
            val = min(val, val)
        self.stackmin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()