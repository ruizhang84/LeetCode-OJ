# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return None
            
        path = []
        dfs(root, k, path)
        
        if len(path) >= k:
            return path[k-1].val


def dfs(root, k, path):
    if len(path) >= k:
        return 
    
    if root.left:
        dfs(root.left, k, path)
        
    path.append(root)
    
    if root.right:
        dfs(root.right, k, path)
        
