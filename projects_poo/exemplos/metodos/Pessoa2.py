# exemplo de método de classe

class Pessoa2:
    numero_de_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa2.numero_de_pessoas += 1

    @classmethod
    def total_de_pessoas(cls):
        print(f"Total de pessoas: {cls.numero_de_pessoas}")

pessoa1 = Pessoa2("Alice", 30)
pessoa2 = Pessoa2("Bob", 25)

Pessoa2.total_de_pessoas()