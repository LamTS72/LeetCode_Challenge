class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in s:
            if i == i.upper():
                i = i.lower()
                res += i
            else:
                res += i

        return res