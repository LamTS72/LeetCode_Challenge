class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        res = 0
        prev_interval = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_interval > intervals[i][0]:
                res += 1
            else:
                prev_interval = intervals[i][1]
        return res