class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps, mapt = {}, {}
        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = t[i]
            elif maps[s[i]] != t[i]:
                return False
                
            if t[i] not in mapt:
                mapt[t[i]] = s[i]
            elif mapt[t[i]] != s[i]:
                return False            
        
        return True    
        
        
        
        
        
