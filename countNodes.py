# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        #root
        if root.right == None:
            if root.left == None:
                return 1
            else:
                return 2
                
                
        #left
        h = 0
        head = root
        while head:
            h += 1
            head = head.left
        
        #right
        temp = 0
        head = root
        while head:
            temp += 1
            head = head.right
        
        if temp == h:
            return (1<<temp) -1
        
        
        left, right = 1, 1<<temp #2**temp
        while left < right:
            mid = (left + right)/2
            if dfs(root, temp, mid):             # not empty
                left = mid + 1
            else:                               # empty
                right = mid - 1
                

        if dfs(root, temp, (left+right)/2):          #not empty
            return (1<<temp) + (left+right)/2 -1
            #return 2**(h-1) + (left+right)/2 -1

        #return 2**(h-1) + (left+right)/2 -2
        return  (1<<temp) + (left+right)/2 -2
        
        
def dfs(root, height, target):
    if height == 0:
        if root == None:           # empty
            return False
        return True
        
    #split = 2**(height-1)
    split = 1<<height-1
    if target <= split:
        return dfs(root.left, height-1, target)
    else:
        return dfs(root.right, height-1, target-split)
        
        
