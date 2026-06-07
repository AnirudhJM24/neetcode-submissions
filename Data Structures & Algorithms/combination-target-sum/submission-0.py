class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i,arr,summ):

            if summ == target:
                res.append(arr.copy())
                return
            
            if i>=len(nums) or summ>target:
                return
            
            arr.append(nums[i])
            dfs(i,arr,summ+nums[i])

            arr.pop()
            dfs(i+1,arr,summ)
        
        dfs(0,[],0)
        return res
        