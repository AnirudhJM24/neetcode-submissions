# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inord = []
        def traverse(root):
            nonlocal inord
        
            if not root:
                return
            
            left = traverse(root.left)
            inord.append(root.val)
            right = traverse(root.right)
        
        traverse(root)

        return inord[k-1]
        

