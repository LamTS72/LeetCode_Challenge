class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution: loop
        # Requirement: O(n)
        iproduct = 1
        for num in nums:
            if num != 0:
                iproduct *= num
        res = len(nums)*[None]
        count_zero = nums.count(0)
        for i in range(len(nums)):
            if nums[i] == 0:
                res = len(nums)*[0]
                if count_zero > 1:
                    return res
                else:
                    res[i] = iproduct
                    return res
            else:
                res[i] = int(iproduct/nums[i])
        return res

        
