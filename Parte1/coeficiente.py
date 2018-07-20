def fatorial (x):
    i=1
    fatorial = 1
    while i <= x :
        fatorial = i * fatorial
        i = i + 1
    return fatorial

def numero_binomial(n , k ):
    return fatorial(n) // (fatorial(k) *fatorial(n-k))

def testa_fatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 2")
    

numero = int(input("Digite um numero:"))

print (fatorial(numero))

testa_fatorial()

numero_binomial(5,3)