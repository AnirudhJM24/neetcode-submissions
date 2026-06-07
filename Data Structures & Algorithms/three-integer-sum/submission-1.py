class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        def binsearch(arr, targ, lo):
            l, r = lo, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == targ:
                    return True
                elif arr[m] < targ:
                    l = m + 1
                else:
                    r = m - 1
            return False

        def twosum(arr, s, start):
            pairs = []
            prev = None
            for i in range(start, len(arr)):
                x = arr[i]
                if prev is not None and x == prev:
                    continue  # skip duplicate x values
                prev = x

                y = s - x
                if binsearch(arr, y, i + 1):   # must be after i
                    pairs.append((x, y))
            return pairs

        prev_i = None
        for j in range(len(nums)):
            i = nums[j]
            if prev_i is not None and i == prev_i:
                continue  # skip duplicate fixed i
            prev_i = i

            target = -i
            pairs = twosum(nums, target, j + 1)  # start after j
            for x, y in pairs:
                ans.append([i, x, y])

        return ans



            
