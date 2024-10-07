class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        i0 = newInterval[0]
        i1 = newInterval[1]
        res = []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            print(intervals[i][0],newInterval[0])
            i0 = min(intervals[i][0], i0)
            i1 = max(intervals[i][1], i1)
            i += 1
        res.append([i0, i1])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
        