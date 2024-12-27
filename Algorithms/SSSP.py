# Note SSSP : Means Single Source Shortest Path

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


# SS BFS -> Single Source BFS can be used as shortest path algorithm for non weighted graph or if all edges have same weight

# Dijkstra's Algorithm -> Single source shortest path algorithm for weighted graphs
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



    
def dijkstra_source_to_target(graph : Graph, source : int, target : int) -> tuple[int,list[int]]:
    """
    input -> graph,source,target
    output -> tuple of 2 element (shortest distance path from source to target, list of path)
    """

    assert 0<=source<graph.size , "source is not in graph"
    assert 0<=target<graph.size , "target is not in graph"

    n = graph.size
    vis = [False]*n
    dis = [float('inf')]*n
    par = [i for i in range(n)]
    par[source]=-1
    pq = PriorityQueue()


    dis[source]=0
    pq.put((0,source))

    while(not pq.empty()):
        curr_dis,curr = pq.get()
        vis[curr]=True
    
        for weight,nxt in zip(graph.weight[curr],graph.data[curr]):
            if(dis[curr]+weight < dis[nxt]):
                dis[nxt]=dis[curr]+weight
                par[nxt]=curr
            if(not vis[nxt]):
                pq.put((dis[nxt],nxt))
    
    path = []
    curr = target 
    if(par[curr]!=curr):              
        while(curr!=-1):
            path.append(curr)
            curr=par[curr]
    
    path.reverse()
    return (dis[target],path)




n = 6
edges = [[0,1,4],[0,2,2],[1,2,5],[1,3,10],[2,4,3],[4,3,4],[3,5,11]]

graph = Graph(n,edges,directed=True)

dis = dijkstra(graph,0)

print(dis)
x=dijkstra_source_to_target(graph,0,5)

print(x)



