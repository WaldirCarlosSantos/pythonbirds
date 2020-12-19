class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão.'

class Mutante(Pessoa):
    olhos = 4

if __name__ == '__main__':
    waldir = Mutante(nome = 'Waldir')
    antonio = Homem(waldir, nome = 'Antônio')
    print(Pessoa.cumprimentar(antonio))
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:
        print(filho.nome)
    antonio.sobrenome = 'José'
    del antonio.filhos
    antonio.olhos = 1
    del antonio.olhos
    print(antonio.__dict__)
    print(waldir.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(antonio.olhos)
    print (waldir.olhos)
    print(id(Pessoa.olhos), id(antonio), id(waldir))
    print(Pessoa.metodo_estatico(), antonio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), antonio.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(waldir, Pessoa))
    print(isinstance(waldir, Homem))

    print(waldir.olhos)

    print(waldir.cumprimentar())
    print(antonio.cumprimentar())