class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = dict()
        i = 0
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumt = nums[i] + nums[left] + nums[right]
                if sumt == target:
                    return sumt
                elif sumt < target:
                    diff = sumt - target
                    res[abs(diff)] = sumt
                    left += 1
                else:
                    diff = sumt - target
                    res[abs(diff)] = sumt
                    right -= 1
            i += 1
        print(res)
        return res[min(res)]
                
