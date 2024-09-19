class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = len(words)
        for i in range(0, len(words)):
            key = words[i]
            for j in range(0, len(key)):
                if key[j] not in allowed:
                    count -= 1
                    break
        return count
                
