class Solution:
    def maxArea(self, h: List[int]) -> int:

        l,r = 0,len(h)-1
        maxh = 0
        while l<r:
            maxh = max(maxh, (r-l)*min(h[r],h[l]))

            if h[l] >= h[r]:
                r-=1
            elif h[r]>=h[l]:
                l+=1
        
        return maxh
        