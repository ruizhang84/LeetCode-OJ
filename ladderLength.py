class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = dict.fromkeys(wordList, 0)
        queue = [(beginWord, 1)]
        
        while queue:
            s, level = queue.pop(0)
            if s == endWord:
                return level

            for i in range(len(s)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != s[i]:
                        w = s[:i] + c + s[i+1:]
                        if w in wordDict:
                            del wordDict[w]
                            queue.append((w, level +1))
        return 0  
        
        
        
