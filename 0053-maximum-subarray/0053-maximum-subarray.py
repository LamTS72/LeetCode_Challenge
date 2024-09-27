class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        currSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], nums[i] + currSum)
            maxSum = max(currSum, maxSum)
        return maxSum
