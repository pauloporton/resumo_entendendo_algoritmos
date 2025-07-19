def pesquisa_binaria(lista, item):
    baixo = 0 # primeiro valor da lista
    alto = len(lista) - 1 # último valor da lista

    while baixo <= alto: # laço até que se encontre apenas um elemento
        meio = (baixo + alto) // 2 # posição escolhida
        chute = lista[meio]

        if chute == item: # item encontrado
            return meio # retorna posição
        elif chute > item:
            alto = meio - 1
        elif chute < item: 
            baixo = meio + 1

    return None # item não encontrado na lista
            
minha_lista = [2, 3, 4, 7, 9, 12, 14]

print(pesquisa_binaria(minha_lista, 3))