# Desenhe e preencha uma tabela para calcular a maior substring comum entre blue (azul, em inglês) e clues (pistas, em inglês).]

palavra_a = 'blue'
palavra_b = 'clues'

m = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(len(m)):
    for j in range(len(m[0])):
        if palavra_a[i] == palavra_b[j]: 
            m[i][j] = m[i-1][j-1] + 1
        else: 
            m[i][j] = 0

print(m)