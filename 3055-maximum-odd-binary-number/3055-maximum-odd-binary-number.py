class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if s.count('1') == 1:
            return ('0' * s.count('0')) + '1'
        return '1' * (s.count('1') - 1) + ('0' * s.count('0')) + '1'