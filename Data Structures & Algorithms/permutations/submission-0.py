class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        if len(nums) == 2:
            return [nums,nums[::-1]]
        if len(nums) == 1:
            return [nums]
        perms = self.permute(nums[1:])

        res = []
        for p in perms:
            for i in range(len(p)+1):
                pc = p.copy()
                pc.insert(i,nums[0])
                res.append(pc)
        return res