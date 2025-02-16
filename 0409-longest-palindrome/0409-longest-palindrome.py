class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = dict()
        for st in s:
            if st in hashmap:
                hashmap[st] += 1
            else:
                hashmap[st] = 1
        
        odd = False
        length = 0
        for key, freq in hashmap.items():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd = True
        return length + 1 if odd else length
        