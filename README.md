# Trabalho Prático 2 (T2) - Quase Menor Caminho (Almost Shortest Path)

Este repositório contém a solução estruturada e autocontida para o problema **Almost Shortest Path** (Quase Menor Caminho), desenvolvida para a disciplina de Algoritmos em Grafos.

---

##  Informações do Projeto

*   **Nome do Problema:** UVa 12144 - Almost Shortest Path
*   **Link do Problema:** [UVa 12144 (PDF)](https://onlinejudge.org/external/121/12144.pdf)
*   **Linguagem Utilizada:** Python 3.10+
*   **Integrantes do Grupo:**
    *   ISADORA FERREIRA NEVES RIOS
    *   JOAO VICTOR LIRA SARAIVA LEAO
    *   CAUAN GOMES DOS SANTOS BARBOSA

---

##  Estrutura do Repositório

```text
T2/
├── README.md                          
├── src/                               
│   ├── main.py                        
│   ├── dijkstra.py                    
│   ├── solver.py                      
│   ├── submission.py                  
│   └── algs4/                         
│       ├── __init__.py
│       ├── bag.py                     
│       ├── directed_edge.py           
│       └── edge_weighted_digraph.py   
├── evidencias/                        
│   └── accepted.png                   
├── apresentacao/                      
│   ├── apresentacao.html
│   └── apresentação ASP.pdf             
└── dados/                             
    └── entradas_do_problema.txt       
```

---

##  Como Executar a Solução

A solução foi projetada de forma **autocontida**. Isso significa que ela funciona imediatamente sem a necessidade de instalar dependências de terceiros ou bibliotecas externas.

### Pré-requisitos
*   Python 3.8 ou superior instalado.

### Execução via Linha de Comando (com arquivo de dados padrão)
Por padrão, ao executar o script, ele tentará ler automaticamente do arquivo localizado em `dados/entradas_do_problema.txt`. Basta executar o comando abaixo a partir do diretório raiz:

```bash
python src/main.py
```

### Execução via Redirecionamento de Entrada (Modo Juiz Online / Console)
Caso queira passar entradas dinâmicas via console ou arquivo customizado:

```bash
python src/main.py < dados/entradas_do_problema.txt
```

###  Como Executar a Apresentação (Slides Interativos)
A apresentação interativa contém slides dinâmicos e simuladores gráficos do algoritmo de Dijkstra e da filtragem de caminhos mínimos. Para executá-la:
1. Abra a pasta `apresentacao/`.
2. Dê um duplo clique no arquivo `apresentacao.html` para abri-lo diretamente em qualquer navegador moderno (Chrome, Firefox, Edge, Safari, etc.).
3. Navegue entre os slides utilizando as teclas de direção do teclado (`←` e `→`), a barra de espaço, ou os botões do rodapé.
4. Nos slides 2 e 5, interaja com as demonstrações clicando nos botões interativos para ver o Dijkstra atuar e filtrar as arestas ótimas.

---

##  Modelagem do Problema e Representação

### Representação do Grafo
Utilizamos a representação de **Lista de Adjacência** baseada na renomada estrutura clássica `algs4` (Sedgewick & Wayne). 
*   **`DirectedEdge`**: Modela a aresta direcionada, possuindo métodos para consultar a origem (`From()`), o destino (`To()`) e o peso associado (`weight`).
*   **`EdgeWeightedDigraph`**: Modela o dígrafo contendo um vetor de `Bag` (uma coleção iterável eficiente). Cada vértice guarda uma lista de suas arestas incidentes de saída.
*   **Grafo Invertido**: Para otimizar a busca reversa, criamos um grafo transposto (invertido) onde toda aresta direcionada $u \rightarrow v$ é inserida como $v \rightarrow u$ com o mesmo peso.

---

##  Algoritmo e Abordagem

O problema consiste em encontrar a menor distância entre uma origem $S$ e um destino $D$ **após remover todas as arestas que pertencem a qualquer um dos menores caminhos originais**. 

O processo é resolvido em 3 etapas de Dijkstra:

1.  **Dijkstra a partir de $S$ no Grafo Original:**
    *   Calculamos a menor distância de $S$ para todos os vértices do grafo, armazenando em um vetor `distS`.
2.  **Dijkstra a partir de $D$ no Grafo Invertido:**
    *   Calculamos a menor distância de todos os vértices para $D$ de forma eficiente rodando Dijkstra a partir de $D$ no grafo transposto. Armazenamos os resultados em um vetor `distD`.
3.  **Filtragem de Arestas do Menor Caminho:**
    *   Sabemos matematicamente que uma aresta direcionada $(u, v)$ de peso $W$ pertence a **pelo menos um menor caminho** entre $S$ e $D$ se, e somente se:
        $$\text{distS}[u] + W + \text{distD}[v] == \text{distS}[D]$$
    *   Iteramos por todas as arestas e construímos um **Grafo Filtrado** (limpo), excluindo todas as arestas que satisfazem a condição de menor caminho acima.
4.  **Dijkstra Final:**
    *   Executamos um terceiro Dijkstra a partir de $S$ no **Grafo Filtrado** para obter a menor distância até $D$. Este valor será exatamente o **Quase Menor Caminho**.

---

##  Análise de Complexidade

### Complexidade Temporal
*   **Algoritmo de Dijkstra:** Implementado com fila de prioridades mínima baseada em heaps binários (`heapq`), operando em $\mathcal{O}((V + E) \log V)$ no pior caso.
*   **Construção dos Grafos e Filtragem:** $\mathcal{O}(V + E)$ para percorrer as listas de adjacências e testar a propriedade matemática de cada aresta.
*   **Complexidade Total:** $\mathcal{O}((V + E) \log V)$, o que garante uma execução extremamente rápida e dentro do limite de tempo (Time Limit) do UVa Online Judge de forma folgada.

### Complexidade Espacial
*   **Estruturas de Dados:** Mantemos os grafos original, transposto e filtrado na memória, cada um consumindo espaço proporcional a $\mathcal{O}(V + E)$ em listas de adjacência.
*   **Estrutura Auxiliar do Heap:** $\mathcal{O}(V)$ para armazenar os nós na fila de prioridades.
*   **Complexidade Espacial Total:** $\mathcal{O}(V + E)$, altamente econômica e escalável.

---

##  Casos Especiais Tratados

A nossa modelagem e implementação cobrem robustamente todos os casos de borda e situações de exceção previstos no problema:

1.  **Origem e Destino Desconectados (Sem Caminho Inicial):**
    *   *Cenário:* Não há nenhum caminho conectando $S$ a $D$ no grafo de entrada.
    *   *Tratamento:* A primeira execução do algoritmo de Dijkstra detectará que a distância mínima de $S$ até $D$ é igual a `INF` (infinito). O fluxo de controle imediatamente cessa e retorna `-1`, sem necessidade de computações desnecessárias subsequentes.
2.  **Quase Menor Caminho Inexistente:**
    *   *Cenário:* Todas as arestas/caminhos ligando $S$ a $D$ fazem parte de algum menor caminho. Após a filtragem, nenhum caminho alternativo resta.
    *   *Tratamento:* Após remover as arestas filtradas, a terceira execução do Dijkstra retornará que a distância até $D$ é `INF`. O algoritmo trata perfeitamente esta condição, convertendo o resultado para `-1` na saída padrão.
3.  **Múltiplos Menores Caminhos Distintos:**
    *   *Cenário:* Existem diversos caminhos com o mesmo comprimento mínimo, compartilhando ou não algumas arestas.
    *   *Tratamento:* Ao invés de rastrear e remover apenas um único caminho gerado pelo vetor de predecessores (o que falharia em remover outros caminhos mínimos paralelos), a nossa filtragem matemática baseada na igualdade $\text{distS}[u] + W + \text{distD}[v] == \text{distS}[D]$ garante a remoção simultânea e absoluta de **toda e qualquer** aresta integrante de qualquer caminho mínimo do grafo original.
4.  **Ciclos e Autoloops:**
    *   *Cenário:* O grafo contém ciclos de peso positivo ou arestas que ligam um vértice a ele mesmo (autoloops).
    *   *Tratamento:* Graças à implementação de relaxamento no Dijkstra combinada com o controle de distâncias ótimas no Heap binário (`heapq`), ciclos e autoloops redundantes são naturalmente ignorados durante a expansão das distâncias, prevenindo loops infinitos e garantindo corretude total.

---

##  Evidência de Submissão (Accepted)

Abaixo está o registro visual da submissão com o status de **Accepted** no portal de correção UVa Online Judge:

![Accepted Status](evidencias/aceppted.png)
