class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        ss = ''
        for i in s:
            if i.isalnum() and ss!= ' ':
                ss+=i
        ss = ss.lower()
        print(ss)
        l,r = 0, len(ss)-1
        ans = True

        while l<r:
            if ss[l]==ss[r]:
                l+=1
                r-=1
            else:
                ans = False
                break

        return ans
        