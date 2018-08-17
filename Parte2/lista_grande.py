from random import randrange

def lista_grande(n):

    lista = []

    for i in range(n):
        lista.append(randrange(100))

    return lista

