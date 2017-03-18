
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = []
        if root:
            recur_path(root, self.path)

        
    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.path) == 0:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        return self.path.pop()
        
def recur_path(root, path):
    if root.right:
        recur_path(root.right, path)
    path.append(root.val)
    if root.left:
        recur_path(root.left, path)
    
    


