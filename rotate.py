class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 or k%len(nums) == 0:
            return 
        
        size = len(nums)
        k = k%size
        cur = start = size-1
        temp = nums[start]
        for i in range(size):
            if cur - k >= 0:
                nums[cur] = nums[cur-k]
                cur -= k
            else:
                if size+cur-k == start:
                    nums[cur] = temp
                    cur = start = start -1
                    temp = nums[start]
                else:
                    nums[cur] = nums[cur-k]
                    cur = size+cur-k

        nums[cur] = temp
        
        
        
        
