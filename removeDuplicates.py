class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        
        total = 1
        count = 1
        for i in range(1, len(nums)):
            count += 1
            if nums[i] != nums[i-1]:
                count = 1
            if count > 2:
                continue
            
            total += 1
            nums[total-1] = nums[i]

        
        return total
        
