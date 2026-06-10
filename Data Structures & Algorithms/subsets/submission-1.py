class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []

        dtemp = []
        def dfs(i):
            if i >= n:
                ans.append(dtemp.copy())
                return
            
            dtemp.append(nums[i])
            dfs(i+1)
            dtemp.pop()
            dfs(i+1)

        dfs(0)
        return ans  