# calculadora de IMC com tipo de imc

class Usuario2:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura * self.altura)
        return imc

    def imprimir_tipo_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            print(f"\nVocê está abaixo do peso normal: {self.nome}, {imc:.2f} ")
        elif imc >= 18.5 and imc <= 24.9:
            print(f"\nVocê está no peso normal: {self.nome}, {imc:.2f} ")
        elif imc >= 25 and imc <= 29.9:
            print(f"\nVocê está no soprepeso: {self.nome}, {imc:.2f} ")
        elif imc >= 30.0 and imc <= 34.9:
            print(f"\nVocê está na obesidade grau 1: {self.nome}, {imc:.2f} ")
        elif imc >= 35.0 and imc <= 39.9:
            print(f"\nVocê está no obesidade grau 2: {self.nome}, {imc:.2f} ")

if __name__ == '__main__':
    nome = input("Digite o seu nome: ")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    usuario2 = Usuario2(nome, peso, altura)
    usuario2.imprimir_tipo_imc()
