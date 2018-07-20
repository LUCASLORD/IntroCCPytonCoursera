import math

a = int(input("Digite o valor de A: "))

b = int(input("Digite o valor de B: "))

c = int(input("Digite o valor de C: "))

delta = math.sqrt(pow(b,2) - (4*a*c))

if delta > 0:
    xUm = (-b + delta) / (2*a)
    xDois = (-b - delta) / (2*a)
    print("As raizes são X':",xUm, "X'':",xDois)

if delta == 0:
    print("Possui apenas uma raiz X': ", xUm)

if delta < 0:
    print("não possui raiz")

