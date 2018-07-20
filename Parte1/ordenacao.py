numeroUm = int(input("Digite um Primero número inteiro: "))
numeroDois = int(input("Digite um Segundo número inteiro: "))
numeroTres = int(input("Digite um Terceiro número inteiro: "))

if numeroTres > numeroDois and numeroDois > numeroUm:
    print("Crescente")
else:
    print("Não Está em Ordem Crescente")
