class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        count = 0
        maps = {}
        #contain = {}
        union = {}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0 and grid[i][0] == '1':
                    count += 1
                    #contain[count] = [(i,0)]
                    maps[(i,0)] = count
                    if i > 0 and grid[i][0] == grid[i-1][0]:
                        if maps[(i,0)] not in union:
                            union[maps[(i,0)]] = [ maps[(i-1,0)] ]
                        else:
                            union[maps[(i,0)]].append(maps[(i-1,0)])
                            
                    
                elif j > 0 and grid[i][j] == '1':   
                    if grid[i][j] == grid[i][j-1]:
                        #contain[count].append((i,j))
                        maps[(i,j)] = count
                    else:
                        count += 1
                        #contain[count] = [(i, j)]
                        maps[(i,j)] = count
                    
                    if i > 0 and grid[i][j] == grid[i-1][j]:
                        if maps[(i,j)] not in union:
                            union[maps[(i,j)]] = [ maps[(i-1,j)] ]
                        else:
                            union[maps[(i,j)]].append(maps[(i-1,j)])
                    
        if count < 2:
            return count

        return handle(count, union)
        
def handle(count, union):
    for i in range(1, count+1):
        if i in union:
            for j in union[i]:
                if j in union:
                    union[j].append(i)
                else:
                    union[j] = [i]
    
    unvisited = [i for i in range(1, count+1)]
    
    count = 0
    while unvisited:
        root = unvisited.pop() 
        count += 1
        queue = [root]
        
        visited = set()
        while queue:
            v = queue.pop()
            visited.add(v)
            if v in unvisited:
                unvisited.remove(v)
        
            if v in union:
                for u in union[v]:
                    if u not in visited:
                        queue.append(u)
    
    
    return count
    
