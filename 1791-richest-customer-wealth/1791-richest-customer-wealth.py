class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_res = 0
        for i in range(len(accounts)):
            temp = sum(accounts[i])
            max_res = max(max_res,temp)
        return max_res

        