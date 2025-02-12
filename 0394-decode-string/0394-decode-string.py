class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        curr_str = ""
        curr_num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append((curr_str, curr_num))
                curr_num = 0
                curr_str = ""
            elif s[i] == "]":
                char, count = stack.pop()
                curr_str = char + (count * curr_str)
            else:
                curr_str += s[i]
        print(curr_str)
        return curr_str
                
                    
