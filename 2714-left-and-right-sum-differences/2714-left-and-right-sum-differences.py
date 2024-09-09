class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return [0]
        rev_nums = nums[::-1]
        leftSum = [0]
        rightSum =[0]

        for i in range(len(nums)-1):
            leftSum.append(leftSum[-1]+nums[i])
            rightSum.append(rightSum[-1]+rev_nums[i])
        rightSum.reverse()
        print(leftSum,rightSum)
        res = [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
        return res