class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)
        
    def pop(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        
    def peek(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
        

    
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()