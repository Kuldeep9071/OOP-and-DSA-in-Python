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



# Examplems


#n1 = 5
#edges1 = [[0,1],[0,4],[1,2],[1,3],[1,4],[2,3],[3,4]]

#g1 = Graph(n1,edges1)

#print(repr(g1))

#n2 = 9
#edges2 = [[0,1,3],[0,3,2],[0,8,4],[1,7,4],[2,7,2],[2,3,6],[2,5,1],[3,4,1],[4,8,8],[5,6,8]]

#g2 = Graph(n2,edges2,directed=True)
#print(repr(g2))
