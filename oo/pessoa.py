class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatistico():
        return 42

    @classmethod
    def nome_eatributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Beijinho na pontinha do Nariz, hihi.'


class Mutante(Pessoa):
    olhos = 3
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return  f'{cumprimentar_da_classe}. Eu sou o amor da vovó'

if __name__ == '__main__':
    bafudinha = Mutante(nome='bafudinha')
    nana = Homem(bafudinha, nome='nana')
    print(Pessoa.cumprimentar(nana))
    print(id(nana))
    print(nana.cumprimentar())
    print(nana.nome)
    print(nana.idade)
    for filho in nana.filhos:
        print(filho.nome)
    nana.sobrenome = 'Bonitinha'
    del nana.filhos
    nana.olhos = 4
    del nana.olhos
    print(nana.__dict__)
    print(bafudinha.__dict__)
    print(Pessoa.olhos)
    print(nana.olhos)
    print(bafudinha.olhos)
    print(Pessoa.metodo_estatistico(), nana.metodo_estatistico())
    print(Pessoa.nome_eatributo_de_classe(), bafudinha.nome_eatributo_de_classe())
    pessoa = Pessoa('anonima')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(nana, Pessoa))
    print(isinstance(nana, Homem))
    print(bafudinha.olhos)
    print(nana.cumprimentar())
    print(bafudinha.cumprimentar())