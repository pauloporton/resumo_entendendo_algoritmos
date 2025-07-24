def quicksort(array):
    if len(array) < 2:
        return array
    else:
        menores = []
        maiores = []
        pivo = array[0]
        for i in array[1:]:
            if i <= pivo:
                menores.append(i)
            else:
                maiores.append(i)
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
