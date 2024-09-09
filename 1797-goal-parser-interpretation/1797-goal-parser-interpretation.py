class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ""
        for i in range(len(command)):
            if command[i] == "(" and command[i+1] == ")":
                res += "o"
            else:
                if command[i] == "(" or command[i] == ")":
                    continue
                else:
                    res += command[i]
        return res
        