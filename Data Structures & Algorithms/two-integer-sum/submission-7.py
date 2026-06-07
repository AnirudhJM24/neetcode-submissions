from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(int)

        for i,n in enumerate(nums):

            seen[n] = i
        
        for idx,i in enumerate(nums):
            n2l = target - i
            if n2l in seen.keys() and seen[n2l]!=idx:
                return [idx,seen[n2l]]
        return []