class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            sum_pt = (point[0])**2 + (point[1])**2
            res.append((sum_pt, point))
        res.sort(reverse=False)
        return [item[1] for item in res[:k]]