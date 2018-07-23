def main():
    carro = Carro("Fusca","amarelo",1950,100)
    carro2 = Carro("Brasilia","preta",1960,90)

    carro.imprime()
    carro2.imprime()


class Carro:

    def __init__(self,modelo, cor, ano, vel_max):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0
        self.vel_max = vel_max

    def imprime(self):
        print("Modelo: {}".format(self.modelo))
        print("Cor: {}".format(self.cor))
        print("Ano: {}".format(self.ano))
        print("Velocidade-Maxima: {}".format(self.vel_max))


main()

