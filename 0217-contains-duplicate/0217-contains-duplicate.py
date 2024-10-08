class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
                if hashmap[num] > 1:
                    return True
            else:
                hashmap[num] = 1
        return False