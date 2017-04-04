class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
            
        if nums[0] != 0:   
            output = [1]
        else:
            output = [0]
        for i in range(1, len(nums)):
            output.append( nums[i-1] * output[i-1])
       
        #print output
        
        prev = nums[-1]
        #reverse order
        for i in range(1, len(nums)):
            output[-i-1] *= prev 
            prev *= nums[-i-1]
            
        return output
        
        
        
