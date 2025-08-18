# Algoritmo de Dijkstra
- A pesquisa em largura é usada para calcular o caminho mínimo para um grafo não ponderado
- O *algoritmo de Dijkstra* é usado para calcular o caminho mínimo para um *grafo ponderado* 
- Cada *aresta* do grafo tem um *número associado* a ela. Eles são chamados de *pesos*
- O algoritmo de Dijkstra funciona quando todos os *pesos são positivos*
- Se o seu grafo tiver pesos negativos, use o algoritmo de Bellman-Ford

# Lógica
1. Encontre o custo mais baixo que ainda não foi processado
2.  Atualize os custos para os seus vizinhos
3. Se qualquer um dos custos for atualizado, atualize também o pai
4. Marque o vértice como processado
5. Volte
