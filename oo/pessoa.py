class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    waldir = Pessoa(nome = 'Waldir')
    antonio = Pessoa(waldir, nome = 'Antônio')
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