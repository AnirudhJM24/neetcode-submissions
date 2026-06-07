class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        l = 0
        c = set()
        maxx = 0

        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l += 1

            c.add(s[r])
            maxx = max(maxx, r - l + 1)

        return maxx
        