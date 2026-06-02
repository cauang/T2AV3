import sys
import heapq



class Bag(list):
    
    def add(self, item):
        self.append(item)

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0


class DirectedEdge:
    
    __slots__ = ('v', 'w', 'weight')
    
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return "%d->%d %.5f" % (self.v, self.w, self.weight)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def From(self):
        return self.v

    def To(self):
        return self.w


class EdgeWeightedDigraph:
    
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




INF = float('inf')

class Dijkstra:
    
    @staticmethod
    def run(grafo: EdgeWeightedDigraph, origem: int) -> list:
        """
        Calcula as menores distâncias a partir de um vértice de origem.
        Retorna uma lista contendo as distâncias mínimas para todos os vértices.
        """
        dist = [INF] * grafo.V
        dist[origem] = 0.0
        
        
        pq = [(0.0, origem)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            
            if d > dist[u]:
                continue
                
            dist_u = dist[u]
            
            for e in grafo.adj[u]:
                v = e.w
                new_dist = dist_u + e.weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
                    
        return dist




class AlmostShortestPathSolver:
    
    def __init__(self, n: int, s: int, d: int):
        self.n = n
        self.origem = s
        self.destino = d
        self.grafo = EdgeWeightedDigraph(n)
        self.grafo_invertido = EdgeWeightedDigraph(n)
        self.lista_arestas = []

    def adicionar_aresta(self, u: int, v: int, p: float):
        
        aresta_normal = DirectedEdge(u, v, p)
        aresta_invertida = DirectedEdge(v, u, p)
        
        self.grafo.add_edge(aresta_normal)
        self.grafo_invertido.add_edge(aresta_invertida)
        self.lista_arestas.append((u, v, p))

    def resolver(self) -> float:
        
        
        distS = Dijkstra.run(self.grafo, self.origem)
        
        
        distD = Dijkstra.run(self.grafo_invertido, self.destino)
        
        menor_caminho_total = distS[self.destino]
        
        
        if menor_caminho_total == INF:
            return -1
            
        
        grafo_filtrado = EdgeWeightedDigraph(self.n)
        for u, v, p in self.lista_arestas:
            
            if distS[u] != INF and distD[v] != INF and distS[u] + p + distD[v] == menor_caminho_total:
                continue  # Aresta proibida, ignora
                
            
            grafo_filtrado.add_edge(DirectedEdge(u, v, p))
            
        
        dist_final = Dijkstra.run(grafo_filtrado, self.origem)
        
        resultado = dist_final[self.destino]
        return -1 if resultado == INF else resultado




def solve():
    
    import os
    
    caminho_dados = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados', 'entradas_do_problema.txt')
    
    if os.path.exists(caminho_dados):
        with open(caminho_dados, 'r') as f:
            input_data = f.read().split()
    else:
        input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    while True:
        try:
            n_str = next(iterator)
            m_str = next(iterator)
        except StopIteration:
            break
            
        n = int(n_str)
        m = int(m_str)
        
        if n == 0 and m == 0:
            break
            
        s = int(next(iterator))
        d = int(next(iterator))
        
        solver = AlmostShortestPathSolver(n, s, d)
        
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            p = float(next(iterator))
            solver.adicionar_aresta(u, v, p)
            
        resultado = solver.resolver()
        
        if resultado == -1:
            print("-1")
        else:
            print(int(resultado))

if __name__ == '__main__':
    solve()
