class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False