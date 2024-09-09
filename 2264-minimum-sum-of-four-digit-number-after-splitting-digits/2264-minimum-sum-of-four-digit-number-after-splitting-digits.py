class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = list(str(num))
        str_num = sorted(str_num)
        print(str_num)
        return int(str_num[0] + str_num[2]) + int(str_num[1] + str_num[3])
        