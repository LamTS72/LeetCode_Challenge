class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            min_a = min(nums)
            if min_a >= k:
                return count
            else:
                count += 1
                nums.remove(min_a)
        return count
        