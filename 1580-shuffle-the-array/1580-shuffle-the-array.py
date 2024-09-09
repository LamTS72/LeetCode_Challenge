class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res.append(i)
            res.append(j)

        return res
