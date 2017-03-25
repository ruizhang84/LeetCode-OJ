class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > 50 or k > 9 or n < (1+k)*k/2:
            return []
        
        ans = []
        temp = []
        for i in range(1, 10):
            temp.append(i)
            dfs(i, n-i, ans, temp, k-1)
            temp.pop()
            
        return ans
        
def dfs(i, n, ans, temp, k):
    if n == 0 and k == 0:
        ans.append(temp[:])
    elif k > 0:
        for j in range(i+1, 10):
            if n-j >=0:
                temp.append(j)
                dfs(j, n-j, ans, temp, k-1)
                temp.pop()
    
        
        
        
        
