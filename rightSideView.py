# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            
        queue = [(root,1)]
        cur = 0
        ans = []
        while queue:
            u, level = queue.pop(0)
            if level == cur + 1:
                cur += 1
                ans.append(u.val)
            if u.right:
                queue.append((u.right, level+1))
            if u.left:
                queue.append((u.left, level+1))
        return ans
            
            
        
        
        
