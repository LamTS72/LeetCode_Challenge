class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    res += 1
        return res
        