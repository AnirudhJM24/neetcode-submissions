class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l,r = 0,k
        n = len(s2)
        while r<=n:
            print(sorted(s2[l:r]))
            if sorted(s1)==sorted(s2[l:r]):
                return True
            else:
                l+=1
                r+=1
        
        return False