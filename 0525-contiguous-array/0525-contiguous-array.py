class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}  
        max_len = count = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap:
                max_len = max(max_len, i - hashmap[count])
            else:
                hashmap[count] = i
        return max_len