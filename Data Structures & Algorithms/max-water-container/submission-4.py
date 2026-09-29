class Solution:
    def maxArea(self, heights: List[int]) -> int:
      left, right = 0, len(heights)-1
      most_water = 0
      while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_water = width * height
        most_water = max(current_water, most_water)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1    
      return most_water  