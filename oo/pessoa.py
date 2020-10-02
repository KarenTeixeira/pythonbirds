class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}!!'


if __name__ == '__main__':
    karen = Pessoa(nome='Karen', idade=28)
    pedro = Pessoa(nome='Pedro', idade=7)
    julia = Pessoa(nome='Julia', idade=4)
    joao = Pessoa(pedro,julia, nome='João', idade=40)
    luiz = Pessoa(karen, nome='Luiz', idade=57)
    print(luiz.nome)
    print(luiz.cumprimentar())
    joao.sobrenome = 'Silva'
    print(luiz.__dict__)
