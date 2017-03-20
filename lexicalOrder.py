class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        start = 1
        for i in range(n):
            ans.append(start)
            start = next_generator(start, n)
        return ans

def next_generator(nums, limit):
    if nums*10 <= limit:  # 1, 2, 3, 4....
        return nums*10
    
    elif (nums+1) % 10 == 0:    # 19, 109, 119, 129, ...
        nums += 1
        while nums%10 == 0:
            nums /= 10
        return nums
        
    elif nums < limit:          # 11, 12, 13, 14, 
        return nums+1
        
    else:
        nums = nums/10+1
        while nums%10 == 0:
            nums /= 10
        return nums
        
        
        
        
