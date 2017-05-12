class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0, 1, 1, 2]
        loop = [1, 1]
        
        if num < 4:
            return ans[:num+1]
        
        base = 0
        while len(ans) <= num:
            temp = [i + loop[base] for i in ans]

            ans.extend(temp)
            base = (base+1) %2
            
        
            
        return ans[:num+1]
        
        
        
