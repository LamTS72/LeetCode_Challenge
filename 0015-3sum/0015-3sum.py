class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution: loop
        # Requirement: O(n^2)
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            ileft = i + 1
            iright = len(nums) - 1
            while ileft < iright:
                isum = nums[i] + nums[ileft] + nums[iright]
                if isum < 0:
                    ileft += 1
                elif isum > 0:
                    iright -= 1
                else:
                    res.add((nums[i], nums[ileft], nums[iright]))
                    ileft += 1
                    iright -= 1
        return list(res)
