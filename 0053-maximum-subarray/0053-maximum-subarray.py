class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)
        maxSum = currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], nums[i] + currSum)
            maxSum = max(currSum, maxSum)
        return maxSum

        