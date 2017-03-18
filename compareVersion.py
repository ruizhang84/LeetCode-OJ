class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        start1, start2, len1, len2 = 0, 0, 0, 0
        while len1 < len(version1) and len2 < len(version2):
            while len1< len(version1) and version1[len1] != '.' :
                len1 += 1
            while len2 < len(version2) and version2[len2] != '.':
                len2 += 1
            
            if int(version1[start1:len1]) < int(version2[start2:len2]):
                return -1
            elif int(version1[start1:len1]) > int(version2[start2:len2]):
                return 1
            len1, len2 = len1+1, len2+1
            start1, start2 = len1, len2
            
        while len1 < len(version1):
            while len1< len(version1) and version1[len1] != '.' :
                len1 += 1
            if int(version1[start1:len1]) != 0:
                return  1
            len1 = len1+1
            start1 = len1
            
        while len2 < len(version2):
            while len2< len(version2) and version2[len2] != '.' :
                len2 += 1
            if int(version2[start2:len2]) != 0:
                return  -1           
            len2 = len2+1
            start2 = len2
            
        return 0
        
        
        
        
