class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
       
        max_length = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                
                max_length = max(length, max_length)
        return max_length

