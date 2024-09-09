class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] in stones[j]:
                    res += 1
        return res
        