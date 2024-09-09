class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res_list = []
        res = ""
        for i, j in zip(s,indices):
            res_list.append([j,i])
        print(res_list)
        res_list.sort()

        for i in range(len(res_list)):
            res += res_list[i][1]

        return res
