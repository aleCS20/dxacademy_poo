#exemplo de getters e setters
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print("nome inválido")

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade Inválida")

pessoa = Pessoa("João", 30)
print(pessoa.get_nome())
print(pessoa.get_idade())

pessoa.set_nome("Maria")
print(pessoa.get_nome())
print(pessoa.get_idade())

