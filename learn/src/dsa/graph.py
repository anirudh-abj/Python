from heap import heap

class Graph:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed
        self.__num_islands = 0

    def add_vertex(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            raise ValueError(f"{node1} not in the graph")
        
        if node2 not in self.graph:
            raise ValueError(f"{node2} not in the graph")
        
        self.graph[node1].append(node2)

        if not self.directed:
            self.graph[node2].append(node1)

    def bfs(self, source):
        if source not in self.graph:
            raise ValueError(f"source - {source} not in graph")
        queue = [source]
        visited = set()
        res = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                queue += self.graph[curr]
                visited.add(curr)
                res.append(curr)

        if len(visited) != len(self.graph):
            nodes = set(list(self.graph.keys()))
            nodes_not_yet_traversed = nodes - visited

        print(res)
        return res
    
    def dfs(self, source):
        if source not in self.graph:
            raise ValueError(f"source - {source} not in graph")
        
        stack = [source]
        visited = set()
        res = []
        while stack:
            curr = stack.pop()
            if curr not in visited:
                stack += self.graph[curr]
                visited.add(curr)
                res.append(curr)

        print(res)
        return res  
    
    def dfs_recursive(self):
        pass 

    def bfs_recursive(self):
        pass  

    def num_islands(self):
        pass









    
        
    

