class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        
        if len(nums) < k:
            for i in range(k):
                tmp = nums[-1]
                nums[1:] = nums[:-1]
                nums[0] = tmp
            return nums
        else:
            modulo = k % len(nums)
            tmp = nums[:-k]
            nums[:k] = nums[-k:]
            nums[k:] = tmp
            return nums