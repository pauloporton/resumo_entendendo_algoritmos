# 4.1 - função soma
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])


# 4.2 - função encontra elementos
def conta_elementos(lista):
    if lista == []:
        return 0
    return 1 + conta_elementos(lista[1:])


# 4.3 - valor mais alto lista
def maximo(lista):
    if len(lista) == 2: # caso base
        if lista[0] > lista[1]:
            return lista[0]
        else:
            return lista[1]        
    sub_max = maximo(lista[1:]) # caso recursivo
    if lista[0] > sub_max:
        return lista[0]
    else:
        return sub_max