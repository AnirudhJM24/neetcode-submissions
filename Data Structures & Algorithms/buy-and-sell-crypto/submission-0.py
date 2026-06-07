class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0

        while r<len(prices):
            if prices[r]<=prices[l]:
                l=r
            else:
                maxp = max(prices[r]-prices[l],maxp)
            r+=1        
        return maxp