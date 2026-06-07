# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        q.append(root)
        fin = []

        while q:
            n = len(q)
            lev = []

            for i in range(n):
                n = q.popleft()
                if n:
                    lev.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if len(lev):
                fin.append(lev)

        return fin

