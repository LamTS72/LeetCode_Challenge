class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    ans.append((i,j))
        return len(ans)

        