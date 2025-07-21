# exemplo 1 (contagem regressiva)
def regressiva(i):
    print(i)
    if i <= 1: 
        return # caso base (interrompe o loop infinito)
    else: 
        regressiva(i-1) # caso recursivo (a função chama a si mesma)


# exemplo 2 (saudação)
def sauda2(nome):
    print(f'Como vai {nome} ?')


def tchau():
    print('ok, tchau!')


def sauda(nome):
    print (f'Olá, {nome}!')
    sauda2(nome) # função sauda2 adicionada ao topo da pilha. quando concluída, é retirada.
    print('preparando para dizer tchau...')
    tchau() # função tchau adicionada ao topo da pilha. quando concluída, é retirada.
        