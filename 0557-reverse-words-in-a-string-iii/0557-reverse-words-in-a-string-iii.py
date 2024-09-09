class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        print(s)
        tmp_s = []
        for i in s:
            tmp_s.append(i[::-1])
        print(tmp_s)
        res = ""
        for i,j in zip(tmp_s,range(len(tmp_s))):
            if j == 0:
                res += i
            else:
                res += " "
                res += i
        return res