class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        vowels = set(['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U'])
        p1 = 0
        p2 = len(s) -1
        
        s = list(s)
        while p1 < p2:
            #forward
            while p1 < p2 and s[p1] not in vowels:
                p1 += 1
            
            #backward
            while p2 > p1 and s[p2] not in vowels:
                p2 -= 1
        
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
            
        return "".join(s)    
        
        
