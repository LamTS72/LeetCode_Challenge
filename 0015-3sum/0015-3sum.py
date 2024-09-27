class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort(reverse=False)
        print(nums)
        n = len(nums) - 2
        i = 0
        res = []
        while i < n:
            if i >= 1 and nums[i] == nums[i-1]:
                i += 1
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    triple0, triple1, triple2 = nums[i], nums[left], nums[right]
                    res.append([triple0, triple1, triple2])
                    while left < right and nums[left] == triple1:
                        left += 1
                    while left < right and nums[right] == triple2:
                        right -= 1
            i += 1
        print(res)

        return res

