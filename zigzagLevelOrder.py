# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        ans = []
        queue = [ root, 0 ]
        level = 0
        while len(queue) != 0:
            idx = queue.pop()
            v = queue.pop()

            if idx >= len(ans):
                  ans.append([v.val])
            elif idx%2 != 0:
                ans[idx].append(v.val)
            else:
                ans[idx].insert(0, v.val)
                
            if v.left != None:
                queue.extend( [v.left, idx+1] )
            if v.right != None:
                queue.extend( [v.right, idx+1] )

                    

        return ans
     
