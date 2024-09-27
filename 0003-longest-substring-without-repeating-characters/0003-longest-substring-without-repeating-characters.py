class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
    
        res = 0
        for i in range(0,len(s) - 1):
            sub_s = s[i]
            max_len = 1
            for j in range(i+1, len(s)):
                if s[j] not in sub_s:
                    sub_s += s[j]
                    max_len += 1
                    
                else:
                    break
            res = max(res, max_len)
        return res


        