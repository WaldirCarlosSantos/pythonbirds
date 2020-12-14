class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

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
    print(antonio.__dict__)
    print(waldir.__dict__)