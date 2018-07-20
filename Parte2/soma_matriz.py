def linha(m):
    linha = len(m)
    return linha

def coluna(m):
    coluna = len(m[0])
    return coluna

def soma_matrizes(m1, m2):
    if linha(m1) == linha(m2) and coluna(m1) == coluna(m2):
        matriz = []
        for i in range(linha(m1)):
            linhas = []
            for j in range(coluna(m2)):
                linhas.append(m1[i][j]+m2[i][j])
            matriz.append(linhas)
        return(matriz)
    else:
        return False
