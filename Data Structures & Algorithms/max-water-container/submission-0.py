class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        while l < r:
            d=r-l
            m=min(heights[l], heights[r])
            f=d*m
            if f>res:
                res=f
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return res                
        