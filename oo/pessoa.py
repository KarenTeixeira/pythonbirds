class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}!!'


if __name__ == '__main__':
    p = Pessoa('Karen', 28)
    print(p.cumprimentar())
    print(p.idade)