class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        max_length = 0
        for i in range(len(s) - 1):
            tmp_s = s[i]
            length = 1
            for j in range(i + 1, len(s)):
                if s[j] not in tmp_s:
                    tmp_s += s[j]
                    length += 1
                else:
                    break
            max_length = max(max_length, length)
        return max_length


        