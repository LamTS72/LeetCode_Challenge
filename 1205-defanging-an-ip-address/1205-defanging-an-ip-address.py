class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ""
        for i in address:
            if i != ".":
                res += i
            else:
                tmp = "[" + i + "]"
                res += tmp
        return res