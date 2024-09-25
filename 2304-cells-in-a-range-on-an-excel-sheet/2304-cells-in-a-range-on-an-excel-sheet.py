class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        start_row = int(s[1])
        end_row = int(s[-1])
        start_col = s[0]
        end_col = int(ord(s[-2]) - ord(s[0]) + 1)
        for i in range(end_col):
            for j in range(start_row, end_row+1):
                string = str(chr(ord(start_col) + i)) + str(j)
                res.append(string)
        return res
