class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        minus_res = 0
        for i in words:
            for j in range(len(i)):
                if i[j] not in allowed:
                    minus_res += 1
                    break
        return len(words) - minus_res

        