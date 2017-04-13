class Solution(object):
    def wordPattern(self, pattern, strs):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pos = 0
        size = 0
        maps = {}
        strsets = set()
        temp = ''
        
        for i in range(len(pattern)):
            while pos < len(strs):
                if strs[pos] != ' ':
                    temp += strs[pos]
                    pos += 1
                else:
                    if pattern[i] not in maps:
                        if temp in strsets:
                            return False
                        maps[pattern[i]] = temp
                        strsets.add(temp)
                    elif maps[pattern[i]] != temp:
                        return False
                    temp = ''
                    pos += 1
                    size += 1
                    break
        
        if size != len(pattern)-1:
            return False
        
        #check the last match
        if pattern[-1] not in maps :
            if temp in strsets:
                return False
        elif maps[pattern[-1]] != temp:
            return False

        return True
            
            
