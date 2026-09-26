class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_water=0
        while left < right :
            width = right- left
            height = min(heights[right], heights[left])
            current = width * height
            max_water=max(max_water, current)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1       
        return max_water    

        