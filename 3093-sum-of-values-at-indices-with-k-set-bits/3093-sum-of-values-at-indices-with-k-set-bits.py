class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i, num in enumerate(nums):
            bin_num = str(bin(i)[2:])
            print(bin_num)
            if bin_num.count("1") == k:
                res += num
        print(res)
        return res