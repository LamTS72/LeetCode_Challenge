class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution:
        # Requirement: O(n)
        hashmap = dict()
        for num in nums: #O(n)
            if num in hashmap: 
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        freq = max(hashmap.values())
        for k, v in hashmap.items():
            if v == freq:
                return k