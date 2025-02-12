class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        s += "+"
        for st in s:
            if st.isdigit():
                num = num * 10 + int(st)
            elif st == " ":
                continue
            else:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    a = stack.pop()
                    stack.append(a*num)
                elif op == "/":
                    a = stack.pop()
                    stack.append(int(a/num))
                op = st
                num = 0
        return sum(stack)

