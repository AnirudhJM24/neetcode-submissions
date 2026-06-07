from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        s = deque()
        ans = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            
            while s and  temp > s[-1][0]:
                print(s[-1][0])
                temp1,index = s.pop()
                print(index,temp1,i,temp)
                ans[index] = i-index
            s.append((temp,i))
            
        
        return ans


        
        