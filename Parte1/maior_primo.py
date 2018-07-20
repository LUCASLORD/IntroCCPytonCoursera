def ePrimo(numero):
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
        return True
    else:
        return False

def maior_primo(x):
    i = 0
    while i <= x:
        if ePrimo(i):
            primo = i
            i = i + 1
        else:
            i = i + 1
    return primo
