class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((end+start)/2)
            if(nums[mid] == target):
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


        