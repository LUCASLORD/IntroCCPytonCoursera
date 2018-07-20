def maiusculas(frase):
    letras = ''
    for i in range(len(frase)):
        if ord(frase[i]) in range(65,91):
            letras += frase[i]
    
    return letras

