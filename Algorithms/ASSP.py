# Note : ASSP means All Source Shortest Path

from queue import PriorityQueue

# Graph Class

class Graph:
    def __init__(self, size: int, edges:list[list[int]], directed=False) -> None:
        self.size = size
        self.directed = directed
        self.weighted = len(edges)>0 and len(edges[0])==3

        self.data = [[] for _ in range(size)]
        self.weight = [[] for _ in range(size)]

        if self.weighted:
            for u,v,w in edges:
                self.data[u].append(v)
                self.weight[u].append(w)

                if not self.directed:
                    self.data[v].append(u)
                    self.weight[v].append(w)
        else:
            for u,v in edges:
                self.data[u].append(v)
                if not self.directed:
                    self.data[v].append(u)


    def __repr__(self) -> str:
        res = ""
        if self.weighted:
            for i,(nodes,weights) in enumerate(zip(self.data,self.weight)):
                res+= "{}: {} \n".format(i,list(zip(nodes,weights)))
        else:
            for i,nodes in enumerate(self.data):
                res+= "{}: {} \n".format(i,nodes)

        return res

    def __str__(self) -> str:

        return __repr__()



# MS BFS -> Multi Source BFS can be used as shortest path algorithm for non weighted graph or if all edges have same weight

# For weighted graph below algorithms can be used

# Dijkstra's Algorithm as ASSP-> Running Single source shortest path algorithm for each node in graph



# Single Source Dijkstra

def dijkstra(graph : Graph, source : int) -> list[int]:
    """
    input -> graph and source
    output -> list with shortest path between source and that (index node)
    """
    n = graph.size
    vis = [False]*n
    dis = [float('inf')]*n
    pq = PriorityQueue()


    dis[source]=0
    pq.put((0,source))

    while(not pq.empty()):
        curr_dis,curr = pq.get()
        vis[curr]=True
    
        for weight,nxt in zip(graph.weight[curr],graph.data[curr]):
            if(dis[curr]+weight < dis[nxt]):
                dis[nxt]=dis[curr]+weight
            if(not vis[nxt]):
                pq.put((dis[nxt],nxt))
    
    return dis


# MultiSource Dijkstra

def MS_dijkstra(graph: Graph) -> list[list[int]]:

    return [dijkstra(graph,source) for source in range(graph.size)]


# Floyd Warshall Algorithm

def Floyd_Warshall(graph: Graph) -> list[list[int]]:

    n=graph.size
    dist = [[float('inf')]*(n) for _ in range(n)]
    
    for i in range(n):
        dist[i][i]=0 
        for j,d in zip(graph.data[i],graph.weight[i]):
            dist[i][j]=d

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(dist[i][k]!=float('inf') and dist[k][j]!=float('inf')  and dist[i][k]+dist[k][j]<dist[i][j]):
                    dist[i][j]=dist[i][k]+dist[k][j]
    
    return dist



n = 6
edges = [[0,1,4],[0,2,2],[1,2,5],[1,3,10],[2,4,3],[4,3,4],[3,5,11]]

graph = Graph(n,edges,directed=True)

dis1 = MS_dijkstra(graph)
dis2 = Floyd_Warshall(graph)

assert dis1==dis2 , f"1 of Dijkstra and Floyd is wrong!"


print("MultiSouruce Dijkstra\n")
for lst in dis1:
    print(lst)
print("\nFloyd\n")
for lst in dis2:
    print(lst)

