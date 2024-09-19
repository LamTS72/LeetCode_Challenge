class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        hashmap = []
        for item in s:
            hashmap.append((item[-1], item[:-1]))
        hashmap.sort()
        s = ""
        for i in range(len(hashmap)):
            s += (" " if i != 0 else "") + hashmap[i][1]
        return s
            