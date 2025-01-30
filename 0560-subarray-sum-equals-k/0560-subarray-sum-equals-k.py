class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        hashmap = {0:1}

        for num in nums:
            sums += num
            if sums - k in hashmap:
                count += hashmap[sums - k]
            
            if sums in hashmap:
                hashmap[sums] += 1
            else:
                hashmap[sums] = 1
        return count

