from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l,r = 0,1
        n = len(s)

        mx = 1

        while r < n:

            c = Counter(s[l:r+1])
            print(c)
            
            t = max(c.values())

            if r-l+1-t<=k:
                mx = max(mx,r-l+1)
                r+=1
                
            else:
                l+=1
            
            
        
        return mx
