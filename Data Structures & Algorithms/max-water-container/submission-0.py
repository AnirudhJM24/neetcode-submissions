class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxh = -1

        for i in range(len(heights)):
            l = i
            r = len(heights)-1

            while r>0:
                maxh = max((r-l)*min(heights[r],heights[l]),maxh)
                r-=1
        
        return maxh

