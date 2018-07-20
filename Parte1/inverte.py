lista = []
cond = True
while cond:
    num  = int(input("Digite um número: "))
    if num != 0:
        lista.append(num)
    else:
        cond = False

for i in range (len(lista), 0, -1):
    print(lista[i-1])