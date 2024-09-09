class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        stack = []
        for i in range(len(s)):
            print(stack)
            if s[i] == "(":
                if s[i] == "(" and len(stack) != 0:
                    res += s[i]
                stack.append(s[i])
            else:
                
                if len(stack) == 0:
                    res += ""
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                    if len(stack) != 0:
                        res += s[i]
                
                    
                        
        return res