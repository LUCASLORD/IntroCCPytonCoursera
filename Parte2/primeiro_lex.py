def primeiro_lex(lista):
    i = 0
    primeiro = lista[0]
    for palavra in lista:
        if len(palavra) == 1:
            if ord(palavra) <= ord(primeiro[0]):
                primeiro = palavra
        elif len(primeiro) == 1:
            if ord(palavra[0]) < ord(primeiro):
                primeiro = palavra
        else:
            for i in range(len(palavra)):
                if ord(palavra[i]) < ord(primeiro[i]):
                    primeiro = palavra
                    i += 1
    return primeiro