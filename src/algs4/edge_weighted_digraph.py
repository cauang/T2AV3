from algs4.bag import Bag

class EdgeWeightedDigraph:
    """
    Grafo direcionado ponderado por arestas.
    Utiliza __slots__ para evitar overhead de dicionário interno.
    """
    __slots__ = ('V', 'E', 'adj')
    
    def __init__(self, v=0):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for i in range(self.V):
            adjs = " ".join([str(x) for x in self.adj[i]])
            s += "%d: %s\n" % (i, adjs)
        return s

    def add_edge(self, e):
        self.adj[e.v].add(e)
        self.E += 1

    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                edges.append(e)
        return edges
