class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        string_a = s.split()
        print(string_a)
        for i in range(k):
            if i == 0:
                res += string_a[i]
            else:
                res += " "
                res += string_a[i]
        return res
        