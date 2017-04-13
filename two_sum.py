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

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = [i]
            else:
                count[nums[i]].append(i) 
        
        for i in range(len(nums)):
            if target-nums[i] in count:
                if count[target-nums[i]][0] != i:
                    return [i, count[target-nums[i]][0] ]
                elif len(count[target-nums[i]]) > 1:
                    return [i, count[target-nums[i]][1] ]
        return []    
           

if __name__=="__main__":
    test=Solution()
    
    print test.twoSum([2,1,9,4,4,56,90,3], 8)

