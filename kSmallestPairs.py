class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
            
        h = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(h, (nums1[i]+nums2[0], [i, 0]))
        
        ans = []
        for i in range(k):
            if len(h) == 0:
                return ans
                
            temp = heapq.heappop(h)
            i,j = temp[1][0], temp[1][1]
            if j < len(nums2)-1:
                heapq.heappush(h, (nums1[i] + nums2[j+1], [i,j+1]))
            ans.append([nums1[i], nums2[j]])
            
        return ans
        
        
