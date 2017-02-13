# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ans = [[] for i in range(n+1)]
        if n == 0:
            return ans[0]

        # n1:
        root = TreeNode(1)
        ans[1].append(root)
        
        if n == 1:
            return ans[1]
        
        # ni:
        for j in range (2, n+1):
            for i in range(1, j+1):
                if i == 1:
                    for base in ans[j-1]:
                        root = TreeNode(i)
                        root.right = increase_tree(base, 1)
                        ans[j].append(root)
                elif i == j:
                    for base in ans[j-1]:
                        root = TreeNode(i)
                        root.left = base
                        ans[j].append(root)
                else:
                    for base_l in ans[i-1]:
                        for base_r in ans[j-i]:
                            root = TreeNode(i)
                            root.left = base_l
                            root.right = increase_tree(base_r, i)
                            ans[j].append(root)

        return ans[n]
        
        
        
def increase_tree(root, num):
    if root == None:
        return 
    temp = TreeNode(root.val + num)
    temp.left = increase_tree(root.left, num)
    temp.right = increase_tree(root.right, num)

    return temp

                        
            

            

        
    
    
