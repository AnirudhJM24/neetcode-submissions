# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        fin = []
        ans = []
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

        for lev in fin:
            ans.append(lev[-1])
        
        return ans
