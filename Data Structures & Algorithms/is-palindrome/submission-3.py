class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = ''.join([i.lower() for i in s if i.isalnum()])
        l,r = 0,len(s)-1
        while l<=r:
            if s[l] == s[r]:
                r-=1
                l+=1
            else:
                return False
        
        return True