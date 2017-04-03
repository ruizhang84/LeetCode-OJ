# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
            
        ans = []
        dfs(root, ans, str(root.val))
        
        return ans
        
def dfs(root, ans, temp):
    if root.left:
        dfs(root.left, ans, temp + "->"+str(root.left.val))
        
    if root.right:
        dfs(root.right, ans, temp + "->"+str(root.right.val))
    
    if root.right == None and root.left == None:
        ans.append(temp)
    
    
    
