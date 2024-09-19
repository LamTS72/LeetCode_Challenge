class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        for item in items:
            if "type" == ruleKey and item[0] == ruleValue:
                count += 1
            elif "color" == ruleKey and item[1] == ruleValue:
                count += 1
            elif "name" == ruleKey and item[2] == ruleValue:
                count += 1
        return count