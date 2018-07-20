xUm = int(input("Digite um Primero número inteiro: "))
yUm = int(input("Digite um Segundo número inteiro: "))
xDois = int(input("Digite um Terceiro número inteiro: "))
yDois = int(input("Digite um Quarto número inteiro: "))

if (yUm - yDois) >= 10 or (yDois - yUm) >= 10:
    print("longe")

else: 
    if (xUm - xDois) >= 10 or (xDois - xUm) >= 10:
        print("longe")  
    else:
        print("perto")
