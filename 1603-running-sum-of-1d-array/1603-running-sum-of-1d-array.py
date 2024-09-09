class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = []
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(nums[i])
                tmp.append(nums[i])
            else:
                res.append(nums[i]+sum(tmp))
                tmp.append(nums[i])
        return res
