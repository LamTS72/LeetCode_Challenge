class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for i in range(len(s)-1):
            res += abs(int(ord(s[i+1])) - int(ord(s[i])))
        return res
        