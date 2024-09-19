class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        list_string = s.split(" ")
        res = ""
        for i in range(k):
            res += " " if i != 0 else ""
            res += list_string[i]
        return res
        