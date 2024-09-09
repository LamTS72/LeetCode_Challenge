class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(t)
        curr = 0
        for i in s:
            if i == t[curr]:
                curr += 1
                if curr == n:
                    return 0
        return n - curr
        