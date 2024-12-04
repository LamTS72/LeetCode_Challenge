class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution: 2 pointers
        # Requirement: less O(n^2)
        hashmap = dict()
        for i, v in enumerate(nums): # O(n)
            hashmap[v] = i
        for i, v in enumerate(nums): # O(n)
            part = target - v
            if part in hashmap and hashmap[part] != i:
                return i, hashmap[part]
                