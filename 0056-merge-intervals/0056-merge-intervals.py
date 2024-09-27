class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        i = 0
        j = 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[j][1], intervals[i][1])
                j += 1
            else:
                res.append(intervals[i])
                i = j
                j += 1
        res.append(intervals[i])
        print(res)
        return res
                



