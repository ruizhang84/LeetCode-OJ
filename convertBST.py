# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        queue = [root]
        total = 0
        while len(queue) > 0:
            node = queue.pop()
            total += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
        temp = 0
        pre_order(root, total, temp)
        return root
    
def pre_order(root, total, temp):
    if root is None:
        return temp
    
    if root.left is not None:
        temp = pre_order(root.left, total, temp)
    
    older = root.val
    root.val = total - temp
    temp += older
    
    if root.right is not None:
        temp = pre_order(root.right, total, temp)
    return temp
    
    
        
        
        
        
