class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            w = j - i
            h = min(height[i], height[j])
            area = h * w
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area