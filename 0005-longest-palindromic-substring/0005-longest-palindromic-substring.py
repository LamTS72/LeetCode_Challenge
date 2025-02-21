class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest_str = s[0]
        
        for i in range(len(s)-1):
            tmp = s[i]
            for j in range(i + 1, len(s)):
                tmp += s[j]
                if tmp == tmp[::-1] and len(longest_str) < len(tmp):
                    longest_str = tmp

        return longest_str