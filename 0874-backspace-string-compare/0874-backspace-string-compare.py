class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True
        stack_s, stack_t = [], []
        for i in range(len(s)):
            if s[i] != "#":
                stack_s.append(s[i])
            else:
                stack_s.pop() if len(stack_s) != 0 else []
        
        for i in range(len(t)):
            if t[i] != "#":
                stack_t.append(t[i])
            else:
                stack_t.pop() if len(stack_t) != 0 else []
        print(stack_s, stack_t)
        return "".join(stack_s) == "".join(stack_t)
