class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        nleft = newInterval[0]
        nright = newInterval[1]
        n = len(intervals)
        res = []
        while i < n and intervals[i][1] < nleft:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= nright:
            nleft = min(intervals[i][0], nleft)
            nright = max(intervals[i][1], nright)
            i += 1
        res.append([nleft, nright])
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
            