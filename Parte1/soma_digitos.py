numero = (input("Digite um número inteiro:"))
soma = 0
i = 0
while i < len(numero):
    soma = soma + int(numero[i])
    i = i + 1 

print(soma)