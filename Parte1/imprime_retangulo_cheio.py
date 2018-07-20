largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))

i = 0
j = 0

while i < altura:
    while j < largura:
        print("#" ,end="")
        j = j + 1
    i = i + 1
    print("")
    j = 0