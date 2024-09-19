class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for i in range(0, len(encoded)):
            arr.append(arr[-1] ^ encoded[i])
        return arr
        