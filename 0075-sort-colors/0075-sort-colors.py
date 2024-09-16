class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums, left, right):
            pIndex = left
            key = nums[right]
            i = left
            while i < right:
                if nums[i] < key:
                    temp = nums[i]
                    nums[i] = nums[pIndex]
                    nums[pIndex] = temp
                    pIndex += 1
                i += 1
            temp = nums[pIndex]
            nums[pIndex] = nums[right]
            nums[right] = temp
            return pIndex
        def quick_sort(nums, left, right):
            if left < right:
                p = partition(nums, left, right)
                quick_sort(nums, left, p - 1)
                quick_sort(nums, p + 1, right)
            return nums
        
        res = quick_sort(nums, 0, len(nums) - 1)
        return res