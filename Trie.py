class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.maps = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp_node = {}
        new_node = {}
        self.maps.add(word)
        #self.maps[word] = 0
        
        if len(self.root) == 0:
            self.root[word] = temp_node
        
        head = self.root
        prev, post = 0, 1
        
        while prev < len(word):
            if post == len(word):
                if word[prev:] not in head:
                    #add node here, common then split
                    for keys in head:
                        if keys[0] == word[prev]:  # split
                            idx = 0
                            while idx < len(keys) and idx + prev < len(word) :
                                if keys[idx] != word[prev + idx]:
                                    break
                                idx += 1
                        
                            # new key contains common sub string
                            if idx < len(keys):
                                head[ keys[:idx] ] = new_node
                                new_node[ keys[idx:] ] = head[keys]  
                                del head[keys]
                                
                                if idx < len(word)-prev:
                                    new_node[ word[prev + idx:] ] = temp_node
                                    
                            else :
                                head[ word[prev + idx:] ] = temp_node
                                
                            return
                        
                    head[ word[prev:] ] = temp_node
                            
                return
                        
            elif word[prev: post] in head:
                head = head[ word[prev: post] ]
                prev = post
                
            post += 1
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.maps:
            return True
            
        return False
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return True
            
        head = self.root
        prev, post = 0, 1
        
        while prev < len(prefix):
            #if prefix[prev:] in head:
            #    return True
            
            if post == len(prefix):
                size = len(prefix) - prev
                for keys in head:
                    if prefix[prev:] == keys[:size]:
                        return True
                            
                return False
                        
            elif prefix[prev: post] in head:
                head = head[ prefix[prev: post] ]
                prev = post
                
            post += 1
        
        return False  
        
        
        
        
