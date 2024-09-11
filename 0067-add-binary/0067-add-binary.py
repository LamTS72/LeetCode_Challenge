class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def toDec(num):
            num = int(num)
            base = 0
            res = 0
            while num > 0:
                mod = num % 10
                power = 2**base
                res += mod * power
                base += 1
                num = num / 10
            return res
        res = bin(toDec(a) + toDec(b))
        return res[2:]


