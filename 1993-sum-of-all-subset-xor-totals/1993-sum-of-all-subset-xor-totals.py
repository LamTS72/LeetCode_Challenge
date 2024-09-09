class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in nums:
            ans |= i
        print (ans)
        return ans * 2**(n-1)