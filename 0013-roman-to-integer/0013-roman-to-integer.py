class Solution:
    def romanToInt(self, s: str) -> int:
        sum_p = 0
        prev = 0
        for ch in s[0:]:
            if ch == "I":
                sum_p += 1
            elif ch == "V":
                sum_p += 5
            elif ch == "X":
                sum_p += 10
            elif ch == "L":
                sum_p += 50
            elif ch == "C":
                sum_p += 100
            elif ch == "D":
                sum_p += 500
            elif ch == "M":
                sum_p += 1000
            if prev == "I" and ch == "V":
                sum_p -= 2
            elif prev == "I" and ch == "X":
                sum_p -= 2
            elif prev == "X" and ch == "L":
                sum_p -= 20
            elif prev == "X" and ch == "C":
                sum_p -= 20
            elif prev == "C" and ch == "D":
                sum_p -= 200
            elif prev == "C" and ch == "M":
                sum_p -= 200
            prev = ch
        return sum_p