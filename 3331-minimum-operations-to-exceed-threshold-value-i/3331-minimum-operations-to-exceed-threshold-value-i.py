class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        return len(list(filter(lambda x: x < k, nums)))