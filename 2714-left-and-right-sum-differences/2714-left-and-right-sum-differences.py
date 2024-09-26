class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i, num in enumerate(nums):
            sumleft = sum(nums[:i])
            sumright = sum(nums[i+1:])
            res.append(abs(sumleft - sumright))
        return res