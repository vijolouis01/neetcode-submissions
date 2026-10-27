class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        most_water = 0
        while left < right:
            current_water = ((right - left) * min(heights[left], heights[right]))
            most_water = max(most_water, current_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return most_water            

        