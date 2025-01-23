class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        j = 1
        res = []
        while j < n:
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[j][1], intervals[i][1])
                j += 1
            else:
                res.append(intervals[i])
                i = j
                j += 1
        res.append(intervals[i])
        return res

            

                



