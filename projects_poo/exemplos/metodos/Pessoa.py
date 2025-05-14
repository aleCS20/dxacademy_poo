# exemplo de método de instância

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos. ")

pessoa = Pessoa("Alice", 20)
pessoa.apresentar()
