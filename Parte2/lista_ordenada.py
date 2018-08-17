def ordenada(lista):

    x = lista[0]
    cond = False
    for i in range(len(lista)):
        if lista[i] >= x:
            cond = True
            x = lista[i]
        else:
            cond = False
            break
    return cond






