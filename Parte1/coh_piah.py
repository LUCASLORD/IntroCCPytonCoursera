import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve 
    uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver 
    o grau de similaridade nas assinaturas.'''
    i = 0
    similaridade = 0
    
    while i < 6:
        similaridade += abs(as_a[i] - as_b[i])
        i += 1

    return similaridade / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
    Inicialmente separar o texto em uma lista de sentenças
    Faremos repetições para executar conforme o número de sentenças, frases, palavras
    Quando separarmos as frases em palavras iremos fazer a contagem de palavras
    e para cada palavra existente iremos contar e somar a quantidade de letras
    Com isso será possível realizar os outros cálculos'''
    quantidade_sentencas = 0
    quantidade_caracteres_sentenca = 0
    tamanho_medio_sentenca = 0
    quantidade_frases = 0
    quantidade_caracteres_frase = 0
    total_de_palavras = 0
    tamanho_total_das_palavras = 0
    tamanho_medio_palavra = 0
    lista_palavras = []
    quantidade_palavras_diferentes = 0
    quantidade_palavras_unicas = 0

    relacao_type_token = 0 #número de palavras diferentes / dividido pelo total de palavras
    razao_hapax_legomana = 0 #número de palavras únicas / dividido pelo total de palavras 
    complexidade_sentenca = 0 #numero de frases / numero de sentencas
    tamanho_medio_frase = 0

    sentencas  = separa_sentencas(texto)
    quantidade_sentencas = len(sentencas)
    teste = len(sentencas[0])
    for sentenca in sentencas:
        
        quantidade_caracteres_sentenca += len(sentenca)
        frases = separa_frases(sentenca)
        quantidade_frases += len(frases)

        for frase in frases:
            
            quantidade_caracteres_frase += len(frase)
            palavras = separa_palavras(frase)
            total_de_palavras += len(palavras)

            for palavra in palavras:
                tamanho_total_das_palavras += len(palavra)
                lista_palavras.append(palavra)
                #print(palavra)
                #print(len(palavra))

    quantidade_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    quantidade_palavras_unicas = n_palavras_unicas(lista_palavras)
    
    tamanho_medio_palavra = tamanho_total_das_palavras / total_de_palavras
    relacao_type_token = quantidade_palavras_diferentes / total_de_palavras
    razao_hapax_legomana = quantidade_palavras_unicas / total_de_palavras
    tamanho_medio_sentenca = quantidade_caracteres_sentenca / quantidade_sentencas
    complexidade_sentenca = quantidade_frases / quantidade_sentencas
    tamanho_medio_frase = quantidade_caracteres_frase / quantidade_frases
    #print(total_de_palavras)
    #print(tamanho_total_das_palavras)
    #print(tamanho_medio_palavra)
    #print(relacao_type_token)
    #print(razao_hapax_legomana)
    #print(tamanho_medio_sentenca)
    #print(complexidade_sentenca)
    #print(tamanho_medio_frase)
    
    return [tamanho_medio_palavra, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentenca,
    complexidade_sentenca, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) 
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass_cpts = []
    similaridade = []
    tamanho_similaridade = 0
    i = 0
    indice = 0
    for texto in textos:
        ass_cpts.append(calcula_assinatura(texto))
    
    for ass_cpt in ass_cpts:
        similaridade.append(compara_assinatura(ass_cp, ass_cpt))

    tamanho_similaridade = len(similaridade)
    for i in range(0,tamanho_similaridade,1):
        if i != tamanho_similaridade - 1:
            if similaridade[i] < similaridade[i+1]:
                indice = i
        else:
            if similaridade[indice] > similaridade[i]:
                indice = i
    return indice + 1


texto = """Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia,
há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões
de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes
de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."""

#ass_cp = calcula_assinatura(texto)
#ass_b = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
#print(compara_assinatura(ass_cp, ass_b))

textos = ['''Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".
Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é
necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero
torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só
quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais
assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer
a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.''',
'''Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o
outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não
falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro,
pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a
falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse,
mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever,
sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.''',
'''NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento,
em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem
eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a
atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da
vida, dando-lhe transparência.''']

#avalia_textos(textos, ass_b)