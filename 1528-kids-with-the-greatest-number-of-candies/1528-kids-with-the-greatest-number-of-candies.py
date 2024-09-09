class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        max_a = max(candies)
        print(max_a)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_a:
                res.append(True)
            else:
                res.append(False)                
        return res
