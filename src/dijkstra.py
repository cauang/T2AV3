import heapq
from algs4.edge_weighted_digraph import EdgeWeightedDigraph

INF = float('inf')

class Dijkstra:
    """
    Classe utilitária para execução do algoritmo de Dijkstra.
    Utiliza heapq nativa de Python para máxima performance.
    """
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
