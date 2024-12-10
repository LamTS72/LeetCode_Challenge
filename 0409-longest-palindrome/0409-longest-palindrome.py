class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Solution: loop
        # Requirement: O(n)
        if len(s) == 1:
            return 1
        hashmap = dict()
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        length = 0
        sub = False
        for k, freq in hashmap.items():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                sub = True
        return length + 1 if sub == True else length