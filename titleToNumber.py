class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for st in s:
            n = ord(st) - 64 + n*26
            
        return n
            
            
            
