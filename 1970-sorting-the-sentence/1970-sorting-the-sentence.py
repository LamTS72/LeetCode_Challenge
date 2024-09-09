class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        res = ""
        map_s = []
        for i in range(len(s)):
            map_s.append((s[i][-1],s[i][:-1]))

        print(map_s)
        map_s.sort()
        for i in range(len(map_s)):
            if i == 0:
                res += map_s[i][1]
            else:
                res += " "
                res += map_s[i][1]


        return res