class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                res += nums[i]
        return res
        