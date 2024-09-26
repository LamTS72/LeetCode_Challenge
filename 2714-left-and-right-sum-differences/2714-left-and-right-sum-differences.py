class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return [0]
        res = []
        for i, num in enumerate(nums):
            sumleft = sum(nums[:i])
            sumright = sum(nums[i+1:])
            res.append(abs(sumleft - sumright))
        return res