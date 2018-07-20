numero = int("Digite um número inteiro")

i = 0 
tamanho = len(str(numero))
while i <= tamanho :
    if i != tamanho : 
        num = int(str(numero[i]))
        numUm = int(str(numero[i+1])
        if num <= numUm :
            if num == numUm :
                print("sim")
                break()
            else:
                i = i + 1
        else:
            print("não")
    else:
        break()