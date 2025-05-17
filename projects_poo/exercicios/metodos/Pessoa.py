#criando uma classe que modele uma pessoa

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura * 100

    def envelhecer(self, ano):
        for _ in range(ano):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, cm):
        self.altura += cm

pessoa = Pessoa("Alessandro", 20, 80, 1.80)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso:.2f} kg, Altura: {pessoa.altura:.2f} m")

pessoa.envelhecer(2)
print(f"Sua idade será: {pessoa.idade} anos, Altura: {pessoa.altura:.2f} m")

pessoa.engordar(3.5)
print(f"Você após engordar terá Peso: {pessoa.peso:.2f} kg")

pessoa.emagrecer(5.5)
print(f"Você depois de emagrecer terá: {pessoa.peso:.2f} kg")