# Tabelas Hash (pontos importantes)

- *dicionários em python*
- Você pode fazer uma tabela hash ao combinar uma função hash com um array
- Colisões são problemas. É necessário haver uma função hash que minimize colisões
- As tabelas hash são extremamente rápidas para pesquisar, inserir e remover itens
- Tabelas hash são boas para modelar relações entre dois itens
- Exemplos de uso: Filtrar duplicatas e memomrização de dados (caching)


# Funções Hash

- A função hash mapeia strings e as relaciona a números (chaves)
- Um nome identificado sempre retorna o mesmo número
- Retorna sempre chaves válidas

# Colisões

- Duas chaves são indicadas para o mesmo espaço
- Para resolver, inicie uma lista encadeada neste espaço
- Se as listas encadeadas se tornem muito longas, o tempo de execução da tabela hash irá piorar

