import math
xUm = 0
xDois = 0

a = int(input("Digite o valor de A: "))

b = int(input("Digite o valor de B: "))

c = int(input("Digite o valor de C: "))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta > 0:
        xUm = (-b + delta) / (2*a)
        xDois = (-b - delta) / (2*a)
        if xUm > xDois:
            print("as raizes da equação são",xDois, "e",xUm)
        else :
            print("as raizes da equação são",xUm, "e",xDois)
    else :
        if delta == 0:
            print("a raiz desta equação é", xUm)

