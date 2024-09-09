class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        n = len(s)
        for i in range(n):
            print(s[i])
            if s[i] == "i":
                res = res[i::-1]
                print("rs ",res)
            else:
                res += s[i]
                print("res :",res)
        return res
        