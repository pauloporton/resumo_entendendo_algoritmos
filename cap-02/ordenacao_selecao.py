def busca_menor(arr): # encontra o menor valor na lista
    menor = arr[0] 
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice # retorna o indice do menor valor

def ordenacao_selecao(arr):
    novoArr = [] # cria nova lista ordenada
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr[menor]) # adiciona o menor valor para a nova lista
        arr.pop(menor) # deleta o menor valor da lista original para continuar o laço
    return(novoArr) # retorna a lista ordenada

print(ordenacao_selecao([7, 3, 5, 1, 8, 10]))
