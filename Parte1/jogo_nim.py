#função que faz jogadas do usuário
def usuario_escolhe_jogada(n,m):
    j = m + 1
    while j > m:
        j = int(input("Quantas peças você vai tirar? "))
        if j <= m and j > 0:
            return j
        else:
            print("Oops! Jogada inválida! tente de novo.")
            j = m + 1

#função que faz jogada do computador
def computador_escolhe_jogada(n,m):
    if (n-1) % (m+1) == 0:
        return 1
    else:
        if n - m == 1 or n % (m + 1) == 0:
            return 0
        else: 
            if n <= m :
                return n
            else:
                return m 

#função principal
def partida():
    i = 1
    j = 0
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) == 0:
        print("Você começa! ")
        while n >= 0:
            if n > 0:
                j = usuario_escolhe_jogada(n,m)
            #teste para saída caso seja mais q uma peça
                if j >= 1:
                    print("Você tirou",j,"peças")
                    n = n - j
                    if n > 0 :
                        print("Agora restam",n,"peças no tabuleiro")
                else:
                    print("Voce tirou",j,"peça.")
                    n = n - j
                    if n > 0 :
                        print("Agora restam",n,"peças no tabuleiro")
            #teste para continuar jogo
                if n >= 1 :
                    j = computador_escolhe_jogada(n,m)
                    if j >= 1 :
                        print("O computador tirou",j,"peças.")
                        n = n - j
                        if n > 0 :
                            print("Agora restam",n,"peças no tabuleiro")
                    else:
                        print("O computador tirou",j,"peça.")
                        n = n - j
                        if n > 0 :
                            print("Agora restam",n,"peças no tabuleiro")
            else:
                print("Fim do jogo! O computador ganhou!")
                break
    else:
        print("Computador começa! ")
        while n >= 0 or n < 0:
            if n > 0:
                j = computador_escolhe_jogada(n,m)
            #teste para saídas caso seja uma peça
                if j >= 1:
                    print("O computador tirou",j,"peças.")
                    n = n - j
                #teste caso tenha peça sobrando
                    if n > 0:
                        print("Agora restam",n,"peças no tabuleiro.")
            #caso não seja maior que uma peça tirada
                else:
                    print("O computador tirou",j,"peça.")
                    n = n - j
                #teste caso tenha peça sobrando
                    if n > 0:
                        print("Agora restam",n,"peças no tabuleiro.")
            #teste para continuar o jogo caso necessário
                if n >= 1:
                    j = usuario_escolhe_jogada(n,m)
                #teste para saídas caso seja uma peça
                    if j > 1:
                        print("Você tirou",j,"peças.")
                        n = n - j
                     #teste caso tenha peça sobrando
                        if n > 0:
                            print("Agora restam",n,"peças no tabuleiro.")
                    else:
                        print("Você tirou",j,"peça.")
                        n = n - j 
                        if n > 0:
                            print("Agora restam",n,"peças no tabuleiro.")
            else:
                print("Fim do jogo! O computador ganhou!")
                break

def campeonato():
    i = 1
    while i < 4:
        print("**** Rodada",i,"****")
        partida()
        i = i + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")


escolha = int(input("Bem-vindo ao jogo do NIM! Escolha: \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato "))

if escolha == 1:
    partida()
else:
    print("Você escolheu um campeonato!")
    campeonato()