import sys
import os

# Ajusta o sys.path para que o pacote 'algs4' e os módulos locais sejam localizados
diretorio_src = os.path.dirname(os.path.abspath(__file__))
if diretorio_src not in sys.path:
    sys.path.insert(0, diretorio_src)

from solver import AlmostShortestPathSolver

def solve():
    """
    Função principal que gerencia o fluxo de entrada e saída.
    Tenta ler de 'dados/entradas_do_problema.txt' se o arquivo existir,
    caso contrário lê da entrada padrão (sys.stdin).
    """
    caminho_dados = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dados', 'entradas_do_problema.txt')
    
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
