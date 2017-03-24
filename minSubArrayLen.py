class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = right = total == 0
        ans = len(nums)+1
        while right < len(nums):
            while total < s and right < len(nums):
                total += nums[right]
                right += 1
            while total >= s:
                ans = min(ans, right-left)
                total -= nums[left]
                left += 1

        if ans == len(nums)+1 :
            return 0
        return ans
        
        
