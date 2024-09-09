class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nums = nums[::-1]
        print(nums)
        return int(nums[0])*int(nums[1]) - int(nums[-1])*int(nums[-2])