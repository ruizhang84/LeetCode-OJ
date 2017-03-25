class TreeNode(object):
    def __init__(self):
        self.word = False
        self.child = {}


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        head = self.root
        for s in word:
            if s in head.child:
                head = head.child[s]
            else:
                head.child[s] = TreeNode()
                head = head.child[s]
                
        head.word = True
        return
        
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        size = len(word) 
        ids = 0
        head = self.root
        while ids < size and word[ids] != '.':
            if word[ids] not in head.child:
                return False
            head = head.child[ word[ids] ]
            ids += 1
            
        if ids == size:
            if head.word:
                return True
            else:
                return False
        
        #DFS    
        queue = []    
        for child in head.child:
            queue.append((head.child[child], ids))
        
        while queue:
            u, idx = queue.pop()
            
            if idx == size-1:
                if u.word:
                    return True
                else:
                    continue
                
            idx += 1
            while idx < size and word[idx] != '.' :
                if word[idx] in u.child:
                    u = u.child[ word[idx] ]
                    idx += 1
                else:
                    break
                
            if idx == size:
                if u.word:
                    return True
                else:
                    continue
                
            if word[idx] == '.':
                for v in u.child:
                    queue.append( (u.child[v], idx)) 
            
                
        return False
