def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        menores = []
        maiores = []
        pivo = lista[0]
        for i in lista[1:]:
            if i <= pivo:
                menores.append(i)
            else:
                maiores.append(i)
        return quicksort(menores) + [pivo] + quicksort(maiores)            


lista = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(lista))