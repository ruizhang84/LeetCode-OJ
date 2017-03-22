        if (len(prerequisites)) == 0:
            return True
            
        maps = [[] for i in range(numCourses)]
        iters = set()
        for req in prerequisites:
            if len(maps[req[1]]) != 0 and req[1] not in iters:
                iters.add(req[1])
            maps[ req[0] ].append(req[1])

        iters = list(iters)
        while iters:
            visited = []
            u = iters.pop()
            if dfs(u, visited, maps):
                return False
            
        return True
        
def dfs(u, visited, maps):
    visited.append(u)
        
    for v in maps[u]:
        if v in visited:
            return True
        else:
            if dfs(v, visited, maps):
                return True

    visited.pop()
    return False
