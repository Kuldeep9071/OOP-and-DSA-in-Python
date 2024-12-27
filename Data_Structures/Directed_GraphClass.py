class Undirected_Graph:
    def __init__(self, n:int, edges:list[list[int]]) -> None:

        self.size = n
        self.data=[[] for _ in range(n)]

        for n1,n2 in edges:
            self.data[n1].append(n2)

    def __repr__(self) -> str:

        return "\n".join(["{}: {}".format(n,neighbors) for n,neighbors in enumerate(self.data)])

    def __str__(self) -> str:

        return self.__repr__()
