class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        res = []
        for i in range(n):
            temp1 = min(nums)
            nums.remove(temp1)
            temp2 = min(nums)
            nums.remove(temp2)
            res.append(temp2)
            res.append(temp1)
        return res
