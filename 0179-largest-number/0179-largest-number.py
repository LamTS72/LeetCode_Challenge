# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         nums = [str(x) for x in nums]
#         nums.sort(reverse=True, key=lambda x: x * 10) 
#         isUsed = [False] * len(nums)
#         max_num = 0
#         def backtracking(num):
#             nonlocal max_num
#             if len(num) == len(nums):
#                 max_num = max(int("".join(num)), max_num)
#                 return 
            
#             for j in range(len(nums)):
#                 if isUsed[j] == False:
#                     num.append(nums[j])
#                     isUsed[j] = True
#                     backtracking(num)
#                     num.pop()
#                     isUsed[j] = False

                
#         if len(nums) == 1:
#             return str(nums[0])

#         num = []
#         backtracking(num)
#         print(max_num)
        
#         return str(max_num)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(0,len(nums)-1-i):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        result = list(map(str, nums))
        return ''.join(result) if nums[0] != 0 else "0"