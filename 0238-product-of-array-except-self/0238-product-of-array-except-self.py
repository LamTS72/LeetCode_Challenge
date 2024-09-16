class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i_c = 0
        p = 1
        for item in nums:
            if item == 0:
                i_c += 1
                continue
            else:
                p *= item
        for i in range(len(nums)):
            if nums[i] == 0:
                nums = [0]*len(nums)
                if i_c > 1:
                    break
                else:
                    nums[i] = p
                    break
            else:
                nums[i] = int(p / nums[i])
        return nums

        
