class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for i in range(len(encoded)):
            res.append(res[-1]^encoded[i])
        return res
        