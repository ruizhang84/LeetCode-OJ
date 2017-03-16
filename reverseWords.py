class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        temp = ''
        for st in s:
            if st != ' ':
                temp += st
            elif temp != '':
                arr.append(temp)
                temp = ''
        if temp != '':
            arr.append(temp)
            
        ans = ''
        if arr:
            ans += arr.pop()
        while arr:
            ans += ' ' + arr.pop()
        return ans
        
        
        
        
