class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort(reverse=False)
        res = []
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r - 1
                else:
                    triplet = [nums[i],nums[l],nums[r]]
                    res.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l = l + 1
                    while l < r and nums[r] == triplet[2]:
                        r = r - 1
        res_f = []
        for item in res:
            if item not in res_f:
                res_f.append(item)
        return res_f