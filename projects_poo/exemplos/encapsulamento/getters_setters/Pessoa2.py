# getters e setters com validação
class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor

try:
    pessoa = Pessoa2("Alice", 30)
    print(pessoa.nome)
    print(pessoa.idade)
    pessoa.idade = -5
except ValueError as e:
    print(e)

try:
    pessoa.nome = ""
except ValueError as e:
    print(e)
