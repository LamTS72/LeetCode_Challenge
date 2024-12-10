class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution: sort
        # Requirement: O(n.log(n))
        return sorted(s) == sorted(t)
