class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.operator(token):
                b = stack.pop()
                a = stack.pop()
                c = self.compute(int(a), int(b), token)
                stack.append(c)
            else:
                stack.append(token)
        return stack.pop()

    def operator(sefl, op):
        if op in ["+", "-", "*", "/"]:
            return True
        else:
            return False

    def compute(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:
            return  int(a / b)


    
