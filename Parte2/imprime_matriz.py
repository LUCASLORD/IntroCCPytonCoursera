def imprime_matriz(matriz):
    '''Recebe uma matriz e imprime formatada'''
    valor = ""
    for linhas in matriz:
        for coluna in linhas:
            valor += str(coluna) + " " 
        valor = valor.strip()
        print(valor)
        valor = ""
