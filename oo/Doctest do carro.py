"""
Exemplo:
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> #testando direção:
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_para_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_para_direita()
>>> direcao.valor
'Sul'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular.velocidade()
0
>>> carro.calcular.direcao()
    'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
    'Leste'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
    'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
    'Oeste'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.velocidade()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_para_a_direita(self):
        self.direcao.girar_para_a_direita()

    def girar_para_a_esquerda(self):
        self.direcao.girar_para_a_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    girar_a_direita_dic = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE
    }
    girar_a_esquerda_dic = {
        NORTE: OESTE,
        OESTE: SUL,
        SUL: LESTE,
        LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_para_direita(self):
        self.valor = self.girar_a_direita_dic[self.valor]

    def girar_para_esquerda(self):
        self.valor = self.girar_a_esquerda_dic[self.valor]
