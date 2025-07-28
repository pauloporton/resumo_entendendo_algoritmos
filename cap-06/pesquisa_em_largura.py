from collections import deque

grafo = {
    "voce": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def pessoa_e_vendedor(nome): # verifica se é vendedor
    return nome[-1] == 'm' # se a última letra for igual a 'm', é vendedor


def pesquisa(nome):
    fila_de_pesquisa = deque() # cria uma lista
    fila_de_pesquisa += grafo[nome] # Adiciona todos os seus vizinhos a lista
    verificadas = [] # registro das pessoas verificadas

    while fila_de_pesquisa: # loop enquanto a fila não está vazia
        pessoa = fila_de_pesquisa.popleft() # pega o primeiro elemento da fila

        if pessoa not in verificadas: # verifica se a pessoa já foi analisada
            if pessoa_e_vendedor(pessoa): # verifica se é um vendedor
                print(f'{pessoa} é um vendedor de manga!') # confirma
                return True
            else:
                fila_de_pesquisa += grafo[pessoa] # não é um vendedor, adiciona mais elementos para verificar
                verificadas.append(pessoa)
    return False # se não houver nenhum vendedor           


pesquisa('voce')

    

