class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        i = 0
        j = 1
        res = []
        while j <len(intervals):
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j = j + 1
            else:
                res.append(intervals[i])
                i = j
                j = j + 1
        res.append(intervals[i])
        return res


