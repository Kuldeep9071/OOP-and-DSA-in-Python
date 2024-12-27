class Undirected_Graph:
    def __init__(self, n:int, edges:list[list[int]]) -> None:

        self.size = n
        self.data=[[] for _ in range(n)]

        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1) 


def DFS(graph : Undirected_Graph,root : int) -> list[int]:
    
    vis = [False for _ in range(graph.size)]
    
    assert 0<=root<graph.size , "root is not there in graph"

    stack = []
    stack.append(root)
    dfs = []

    while(stack):
        curr = stack.pop()
        
        if(not vis[curr]):
            vis[curr]=True
            dfs.append(curr)

            for nxt in graph.data[curr]:
                if(not vis[nxt]):
                    stack.append(nxt)
    
    return dfs


n = 5
edges = [[1,3],[1,0],[0,3],[2,4],[2,3]]

g = Undirected_Graph(n,edges)

print(DFS(g,0))

