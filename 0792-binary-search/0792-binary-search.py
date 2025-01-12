class Solution:
    def iterator_bsearch(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def recursive_bsearch(self, nums, target,left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.recursive_bsearch(nums, target, left + 1, right)
        else:
            return self.recursive_bsearch(nums, target, left, right - 1)
    def search(self, nums: List[int], target: int) -> int:
        print("Iterator Result: ", self.iterator_bsearch(nums, target))
        return self.recursive_bsearch(nums, target, 0, len(nums) - 1)
