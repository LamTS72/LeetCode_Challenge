class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums, left, right):
            key = nums[right]
            pIndex = left
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
 
        def quicksort(nums, left, right):
            if left < right:
                p = partition(nums, left, right)
                quicksort(nums, left, p - 1)
                quicksort(nums, p + 1, right)

        quicksort(nums, 0, len(nums) - 1)
        return nums