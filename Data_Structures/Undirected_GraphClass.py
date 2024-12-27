class Undirected_Graph:
    def __init__(self, n:int, edges:list[list[int]]) -> None:

        self.size = n
        self.data=[[] for _ in range(n)]

        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    
    def __repr__(self) -> str:

        return "\n".join(["{}: {}".format(n,neighbors) for n,neighbors in enumerate(self.data)])

    def __str__(self) -> str:

        return self.__repr__()

#n = 5
#edges = [[1,3],[1,0],[0,3],[2,4],[2,3]]

#g = Undirected_Graph(n,edges)

#print(repr(g))
