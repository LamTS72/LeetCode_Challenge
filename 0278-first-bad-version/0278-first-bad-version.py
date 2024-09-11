# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n 
        v = 1
        
        while low <= high:
            mid = (high + low) // 2
            if isBadVersion(mid) == False :
                low = mid + 1
            else:
                high = mid - 1
                v = mid

        return v