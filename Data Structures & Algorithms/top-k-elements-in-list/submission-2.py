from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for i in count.keys():
            idx = count[i]
            freq[idx].append(i)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            print(freq[i])
            
            res.extend(freq[i])
            if(len(res)==k):
                return res