class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Solution: loop
        # Requirement: O(n)
        if s == "" and t == "": 
            return True
        stack_s = []
        stack_t = []
        i = j = 0
        while i < len(s):
            if s[i] != "#":
                stack_s.append(s[i])
            else:
                if len(stack_s) != 0:
                    stack_s.pop()
            i += 1
        while j < len(t):
            if t[j] != "#":
                stack_t.append(t[j])
            else:
                if len(stack_t) != 0:
                    stack_t.pop()
            j += 1
        return "".join(stack_s) == "".join(stack_t)



