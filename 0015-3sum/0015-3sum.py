class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumt = nums[i] + nums[left] + nums[right]
                if sumt > 0:
                    right -= 1
                elif sumt < 0:
                    left += 1
                else:
                    t1, t2, t3 = nums[i], nums[left], nums[right]
                    res.add((t1, t2, t3))
                    while left < right and nums[left] == t2:
                        left += 1
                    while left < right and nums[right] == t3:
                        right -= 1
        print(res)
        return list(res)
 

        
