from collections import deque

class Undirected_Graph:
    def __init__(self, n:int, edges:list[list[int]]) -> None:

        self.size = n
        self.data=[[] for _ in range(n)]

        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1) 


def Cycle(graph: Undirected_Graph) -> bool:

    n = graph.size
    root = 0;
    par = [-1]*n
    vis = [False]*n
    q = deque()

    q.append(root)
    vis[root]=True

    while(q):
        curr = q.popleft()
        for nxt in graph.data[curr]:
            if(par[curr]!=nxt):
                if(not vis[nxt]):
                    q.append(nxt)
                    vis[nxt]=True
                    par[nxt]=curr
                else:
                    return True

    return False


n = 5
edges = [[0,1],[0,2],[0,3],[3,4],[1,2]]

g = Undirected_Graph(n,edges)

print(Cycle(g))
