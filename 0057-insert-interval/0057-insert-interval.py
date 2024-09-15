class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i0 = newInterval[0]
        i1 = newInterval[1]
        i = 0
        res = []
        #first case
        while i < len(intervals) and intervals[i][1] < i0:
            res.append(intervals[i])
            i = i + 1
        #overlap case
        while i < len(intervals) and intervals[i][0] <= i1:
            i0 = min(i0, intervals[i][0])
            i1 = max(i1, intervals[i][1])
            i = i + 1
        res.append([i0,i1])
        #remains
        while i < len(intervals):
            res.append(intervals[i])
            i = i + 1
        return res
        