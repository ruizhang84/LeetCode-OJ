class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if (len(prerequisites)) == 0:
            return True
            
        graphs = [[] for i in range(numCourses)]
        indegree = [ 0 for i in range(numCourses)]
        #graphs
        for req in prerequisites:
            indegree[req[1]] += 1
            graphs[ req[0] ].append(req[1])

        #count
        count = 0
        
        #iterate by indegree
        iters = []
        for i in range(numCourses):
            if indegree[i] == 0:
                count += 1
                iters.append(i)
        
        while iters:
            u = iters.pop()    
            
            for v in graphs[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    count += 1
                    iters.append(v)
                    
        return count == numCourses
