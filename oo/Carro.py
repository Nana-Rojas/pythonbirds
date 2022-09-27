class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = self.velocidade + 1

    def frear(self):
        self.velocidade = self.velocidade - 2


class Direcao:
    def __init__(self, sentido):
        self.opcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
        if sentido in self.opcoes:
            self.sentido = sentido
        else:
            print('Valor invalido!')

    def girar_para_esquerda(self):
        indice = self.opcoes.index(self.sentido)
        if indice == 0:
            self.sentido = self.opcoes[-1]
        else:
            self.sentido = self.opcoes[indice - 1]

    def girar_para_direita(self):
        indice = self.opcoes.index(self.sentido)
        if indice == 3:
            self.sentido = self.opcoes[0]
        else:
            self.sentido = self.opcoes[indice + 1]

direcao = Direcao(sentido='Sul')
motor = Motor(velocidade=80)

carro = Carro(motor, direcao)
print(carro.direcao.sentido)
carro.direcao.girar_para_direita()
print(carro.direcao.sentido)

