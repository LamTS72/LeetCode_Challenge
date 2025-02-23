class Solution:
    def iterator(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1 
        return -1

    def recursive(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.recursive(nums, target, left, mid - 1)
        else:
            return self.recursive(nums, target, mid + 1, right)

    def search(self, nums: List[int], target: int) -> int:
        print(self.iterator(nums, target))
        return self.recursive(nums, target, 0, len(nums) - 1)