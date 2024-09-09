class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_res = 0
        count = 0
        for i in s:
            if i == "(":
                count += 1
                if count > max_res:
                    max_res = count
            elif i == ")":
                count -= 1
        return max_res