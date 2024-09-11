class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vocab = {}
        for i in range(len(nums)):
            if nums[i] in vocab:
                vocab[nums[i]] += 1
            else:
                vocab[nums[i]] = 1
    
        res = max(vocab.values())
        for i in vocab.keys():
            if vocab[i] == res:
                return i
        