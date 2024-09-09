class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        flag_pair = False
        for i in range(len(s)):
            if s[i] == "*" and flag_pair == False:
                res += 1
            elif s[i] == "*" and flag_pair == True:
                res += 0

            elif s[i] == "|" and flag_pair == False:
                flag_pair = True
            elif s[i] == "|" and flag_pair == True:
                flag_pair = False

        return res

            


        