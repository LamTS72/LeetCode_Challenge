class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i, num in enumerate(nums):
            remain = target - num
            if remain in hashmap and hashmap[remain] != i:
                return i, hashmap[remain]
