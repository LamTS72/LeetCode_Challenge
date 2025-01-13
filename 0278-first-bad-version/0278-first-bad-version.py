# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Solution: binary search
        # Requirement: O(log(n))
        left, right, res = 1, n, 1
        while left <= right:
            mid = (right + left) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
                res = mid
        return res