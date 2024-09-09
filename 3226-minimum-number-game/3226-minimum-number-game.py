class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)/2
        for i in range(n):
            min_A = min(nums)
            nums.remove(min_A)
            min_B = min(nums)
            nums.remove(min_B)
            res.append(min_B)
            res.append(min_A)
        return res

        