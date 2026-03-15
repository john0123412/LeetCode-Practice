class Solution:
    def maxArea(self, height: List[int]) -> int:
        right =len(height)-1
        left = 0
        maxarea = 0
        while left < right:
            maxarea = max(maxarea,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea