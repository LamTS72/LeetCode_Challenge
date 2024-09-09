class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.count('1') == 1:
            return s.count('0')*'0' + '1'

        return (s.count('1')-1)*'1' + s.count('0')*'0' + '1'

        