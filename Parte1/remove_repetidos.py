def remove_repetidos(lista):
    lista.sort()
    cond = True
    while cond:
        for i in range(len(lista)):
            if i != (len(lista) - 1):
                if lista[i] == lista[i+1]:
                    del lista[i]
                    break
            else:
                cond = False      
    return(lista)


