class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for i in range(len(operations)):
            if "++" in operations[i]:
                X += 1
            elif "--" in operations[i]:
                X -= 1
        return X
        