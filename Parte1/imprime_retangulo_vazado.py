largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))

i = 0
j = 0

while i < altura:
    while j < largura:
        if i > 0 and i < (altura - 1):
            if j > 0 and j < (largura - 1):
                print(" ", end="")
                j = j + 1
            else:
                print("#" ,end="")
                j = j + 1
        else:
            print("#" ,end="")
            j = j + 1
    i = i + 1
    print("")
    j = 0