"""
    Two Sum
    """
#Given an array of integers, find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that
#they add up to the target, where index1 must be less than index2.
#Please note that your returned answers (both index1 and index2) are not zero-based.

#You may assume that each input would have exactly one solution.

#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        new_nums = sorted(nums)
        for i in range(len(nums)):
            if new_nums[-i-1] <= target + abs(new_nums[0]):
                index = len(nums)-i-1
                break
        
        first, last = self.match_target(new_nums[0:index+1], 0, index, target)
        
        index = []
        n = 0
        for i in range(len(nums)):
            if nums[i] == new_nums[first] or nums[i] == new_nums[last]:
                index += [i+1]
                n += 1
                if n  == 2:
                    break
        return index
        
    def match_target(self, list, first, last, target):
        if list[first] + list[last] == target:
            return (first, last)
        
        if list[first] + list[last] < target:
            fist, last = self.match_target(list, first+1, last, target)
        elif list[first] + list[last] > target:
            fist, last = self.match_target(list, first, last-1, target)
        return fist, last

if __name__=="__main__":
    test=Solution()
    
    print test.twoSum([2,1,9,4,4,56,90,3], 8)

