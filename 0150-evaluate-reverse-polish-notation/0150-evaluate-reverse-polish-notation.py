class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.check_operator(token):
                b = int(stack.pop())
                a = int(stack.pop())
                c = self.calculate(token, a, b)
                stack.append(c)
                print(str(a) +str(token)+ str(b)+ "=" +str(c))
            else:
                stack.append(int(token))
        return stack.pop()

    def check_operator(self, op):
        if op in ['+', '-', '*', '/']:
            return True
        else:
            return False
    
    def calculate(self, op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return int(a / b)