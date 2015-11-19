class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        temp = 0
        #move to scan
        while (i<=j):
            if height[i] > height[j]:
                if temp < height[j]*(j-i):
                    temp = height[j]*(j-i)
                j -= 1
            else:
                if temp < height[i]*(j-i):
                    temp = height[i]*(j-i)
                i += 1

        return temp
