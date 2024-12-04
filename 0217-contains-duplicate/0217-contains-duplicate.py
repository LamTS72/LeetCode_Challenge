class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution: one loop
        # Requirement: O(n)
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False