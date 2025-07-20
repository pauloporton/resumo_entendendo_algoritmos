# Arrays
- Os elementos são armazenados um ao lado do outro
- Desperdiçam memória
- Mover os itens, caso seja necessário inserir novos itens
- Leitura rápida, inserção e deleção lentas

# Listas Concatenadas
- Armazenamento espalhado pela memória
- Um elemento armazena o endereço do próximo elemento
- Caso você queira saber o último elemento, precisa percorrer todos os elementos
- Leitura lenta, inserção e deleção rápidas

## Comparação Arrays e Listas Concatenadas
|  | Arrays | Listas |
|----------|:--------:|--------:|
| Leitura | O(1) | O(n) |
| Inserção | O(n) | O(1) |
| Eliminação | O(n) | O(1) |

Dica:
- Array: aleatório
- Lista: sequencial

# Resumo Ordenação por Selecão (Crescente)

1. Crie uma nova lista vazia para armazenar a lista ordenada
2. Percorra a lista original e encontre o menor valor por meio de um loop
3. Armazena o índice do menor valor
4. Adicione o menor valor encontrado na nova lista criada no passo 1 usando o método append()
5. Remova o menor valor encontrado da lista original usando o método pop() e o índice encontrado no passo 3
6. Repita os passos 2 a 4 até que a lista original esteja vazia
7. Retorne a nova lista ordenada

- Tempo de execução: O(n * n) = O(n^2)