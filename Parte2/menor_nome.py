def menor_nome(nomes):
    menor = nomes[0].strip()
    i = 0
    for i in range(len(nomes)):
        if len(nomes[i].strip()) < len(menor):
            menor = nomes[i].strip()
    
    return menor.capitalize()        