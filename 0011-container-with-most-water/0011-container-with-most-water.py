class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
