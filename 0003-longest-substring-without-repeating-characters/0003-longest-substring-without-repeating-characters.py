class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 1
        max_l = 0
        for i in range(0, len(s) - 1):
            tmp_l = 1
            tmp_s = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in tmp_s:
                    tmp_s += s[j]
                    tmp_l += 1
                else:
                    break
            max_l = max(max_l, tmp_l)
        return max_l
        