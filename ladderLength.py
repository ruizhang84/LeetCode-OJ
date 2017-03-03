class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = dict.fromkeys(wordList, 0)
        if endWord not in wordDict:
            return 0
        queue_front = set([beginWord])
        queue_back = set([endWord])
        dist = 1
        
        while queue_front and queue_back:
            dist += 1
            if len(queue_front) <= len(queue_back):
                front = set([])
                for s in queue_front:
                    for i in range(len(s)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != s[i]:
                                w = s[:i] + c + s[i+1:]
                                if w in queue_back:
                                    return dist 
                                if w in wordDict:
                                    del wordDict[w]
                                    front.add(w)
                queue_front = front
            else:
                back = set([])
                for s in queue_back:    
                    for i in range(len(s)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != s[i]:
                                w = s[:i] + c + s[i+1:]
                                if w in queue_front:
                                    return dist 
                                if w in wordDict:
                                    del wordDict[w]
                                    back.add(w)
                queue_back = back
            
        return 0   
