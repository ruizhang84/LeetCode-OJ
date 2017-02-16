# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
            
        dummy = TreeNode(0)
        stack = [root]
        while len(stack) != 0:
            v = stack.pop()
            dummy.right = v
            
            if v.right != None:
                stack.append(v.right)
            if v.left != None:
                stack.append(v.left)

            dummy = dummy.right
            dummy.left = None
        
        return dummy.right    

            
            
