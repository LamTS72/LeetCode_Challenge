class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = nums.count(0)
        if count_zero > 1:
            return [0]*len(nums)
        iproduct = 1
        for num in nums:
            if num != 0:
                iproduct *= num
        
        for i in range(len(nums)):
            if nums[i] == 0 and count_zero == 1:
                nums = [0]*len(nums)
                nums[i] = iproduct
                return nums
            else:
                nums[i] = int(iproduct/nums[i])
        print(nums)
        return nums

        
