class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = sum(accounts[0])
        for i in range(1, len(accounts)):
            wealth = max(wealth, sum(accounts[i]))
        return wealth
        