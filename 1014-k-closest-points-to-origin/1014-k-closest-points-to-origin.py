class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for point in points:
            compute = (point[0])**2 + (point[1])**2
            res.append((compute, point))
        res.sort(reverse=False)
        print(res)
        print(res[:k])
        res = [item[1] for item in res[:k]]
        return res
