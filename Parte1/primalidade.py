numero = int(input("Digite um número inteiro:"))

i = 1
j = 0
while i <= numero:
    if numero % i == 0:
        i = i + 1
        j = j + 1
    if i >= (numero/2):
        i = numero
        i = i + 1
        j = j + 1
    i = i + 1
    
if j == 2:
    print("primo")
else:
    print("não primo")
