# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
            
        root = UndirectedGraphNode(node.label)
        visited = set([node])
        maps = {node: root}

        #enqueue
        queue = []
        for v in node.neighbors:
            if v not in visited:
                maps[v] = UndirectedGraphNode(v.label)
                root.neighbors.append(maps[v])
                queue.append(v)
            else:
                root.neighbors.append(root)
        
        

        #bsf
        while queue:
            u = queue.pop()
            s = maps[u]
            visited.add(u)
            
            for v in u.neighbors:
                if v not in visited:
                    if v not in maps:
                        maps[v] = UndirectedGraphNode(v.label)
                    s.neighbors.append(maps[v])
                    if len(queue) == 0 or queue[-1] != v:
                        queue.append(v)
                else:
                    s.neighbors.append(maps[v])
        

        return root
        
        
        
