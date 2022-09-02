class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    Bafudinha = Pessoa(nome='Bafudinha')
    Nana = Pessoa(Bafudinha, nome='Nana')
    print(Pessoa.cumprimentar(Nana))
    print(id(Nana))
    print(Nana.cumprimentar())
    print(Nana.nome)
    print(Nana.idade)
    for filho in Nana.filhos:
        print(filho.nome)
    Nana.sobrenome = 'Bonitinha'
    del Nana.filhos
    Nana.olhos = 4
    del Nana.olhos
    print(Nana.__dict__)
    print(Bafudinha.__dict__)
    Pessoa.olhos = 1
    print(Pessoa.olhos)
    print(Nana.olhos)
    print(Bafudinha.olhos)
