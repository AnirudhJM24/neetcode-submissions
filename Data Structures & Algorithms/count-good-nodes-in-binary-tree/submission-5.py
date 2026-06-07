# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        count = 0
        maxv = -99999999
        q.append((root,maxv))

        while q:
            
            node,maxv = q.popleft()
            if node.val>=maxv:
                count+=1
            if node.left:
                q.append((node.left,max(node.val,maxv)))
            if node.right:
                q.append((node.right,max(node.val,maxv)))

                    
        
        return count
        