class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return sum(num)
        product = 1
        for num in nums:
            if num != 0:
                product *= num
            
        count0 = nums.count(0)
        res = []
        for i,num in enumerate(nums):
            if num == 0:
                res = [0]*len(nums)
                if count0 > 1:
                    return res
                else:
                    res[i] = product
                    return res
            else:
                res.append(int(product / num))
        return res

        
