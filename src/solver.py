from algs4.directed_edge import DirectedEdge
from algs4.edge_weighted_digraph import EdgeWeightedDigraph
from dijkstra import Dijkstra, INF

class AlmostShortestPathSolver:
    """
    Classe que encapsula a lógica para resolver o problema do Quase Menor Caminho.
    """
    def __init__(self, n: int, s: int, d: int):
        self.n = n
        self.origem = s
        self.destino = d
        self.grafo = EdgeWeightedDigraph(n)
        self.grafo_invertido = EdgeWeightedDigraph(n)
        self.lista_arestas = []

    def adicionar_aresta(self, u: int, v: int, p: float):
        """
        Adiciona aresta ao grafo original e ao grafo invertido.
        """
        aresta_normal = DirectedEdge(u, v, p)
        aresta_invertida = DirectedEdge(v, u, p)
        
        self.grafo.add_edge(aresta_normal)
        self.grafo_invertido.add_edge(aresta_invertida)
        self.lista_arestas.append((u, v, p))

    def resolver(self) -> float:
        """
        Executa os 3 passos de Dijkstra para encontrar o Quase Menor Caminho.
        """
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
