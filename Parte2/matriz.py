def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado.'''

    matriz = [] #lista vazia

    for i in range(num_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        #adiciona linha à matriz
        matriz.append(linha)
    
    return matriz

def mostra_matriz(matriz):
    '''Recebe uma matriz e imprime formatada'''
    valor = ""
    for linhas in matriz:
        for coluna in linhas:
            valor += str(coluna) + " " 
        print(valor)
        valor = ""
mostra_matriz(cria_matriz(4,4,0))