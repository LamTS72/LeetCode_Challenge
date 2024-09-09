class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        n = len(items)
        count = 0
        for i in range(n):
            if ruleKey == "type" and ruleValue == items[i][0]:
                count += 1
            elif ruleKey == "color" and ruleValue == items[i][1]:
                count += 1
            elif ruleKey == "name" and ruleValue == items[i][2]:
                count += 1
        return count