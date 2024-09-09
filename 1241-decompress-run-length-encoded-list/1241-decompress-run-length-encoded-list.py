class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_pair = len(nums)/2
        list_pair = []
        res_tmp = []
        res = []
        for i in range(len_pair):
            list_pair.append([nums[2*i],nums[2*i+1]])
        for i in range(len_pair):
            res_tmp.append(list_pair[i][0]*[list_pair[i][1]])
        
        print(res_tmp)
        for i in range(len(res_tmp)):
            res += res_tmp[i]
            print(res_tmp[i])
        return res