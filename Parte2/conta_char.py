def conta_letras(frase, contar="vogais"):
    qtdvogais = 0
    qtdconsoantes = 0
    palavras = frase.split()
    i = 0
    for palavra in palavras:
        for i in range(len(palavra)):
            if palavra[i] in 'aeiou':
                qtdvogais += 1
            else:
                qtdconsoantes +=1
    if contar =='vogais':
        return qtdvogais
    else:
        return qtdconsoantes

