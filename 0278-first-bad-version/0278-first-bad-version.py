# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res, left, right = 1, 0, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
                res = mid
        return res

