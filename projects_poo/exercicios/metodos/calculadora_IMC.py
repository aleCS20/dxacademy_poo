# calculadora de IMC

class Usuario:
    valor_imc = 0.0

    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.valor_imc = self.peso / (self.altura * self.altura)

if __name__ == '__main__':
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    usuario = Usuario(peso, altura)
    print(f"O valor do seu IMC é:  {usuario.valor_imc:.2f}")

