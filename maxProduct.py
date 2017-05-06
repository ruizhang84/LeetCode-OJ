class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = 'abcdefghijklmnopqrstuvwxyz'
        maps = {}
        n = 1
        for st in s:
            maps[st] = n
            n <<= 1
        
        nums = []
        for w in words:
            temp = 0
            for st in w:
                temp |= maps[st]
            nums.append(temp)
            
        #print nums, maps
        
        maxs = 0
        for i in range(len(words)-1):
            for j in range(i, len(words)):
                if nums[i] & nums[j] == 0:
                    maxs = max(len(words[i])* len(words[j]), maxs)
                
        return maxs
                
                
                
