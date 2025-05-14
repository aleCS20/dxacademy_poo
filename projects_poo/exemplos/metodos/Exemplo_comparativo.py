#exemplo comparativo da utilização dos métodos

class Exemplo:
    contador = 0

    def __init__(self, valor):
        self.valor = valor
        Exemplo.contador += 1

    def metodo_instancia(self):
        print(f"Valor da instancia : {self.valor}")

    @classmethod
    def metodo_classe(cls):
        print(f"Contador da classe : {cls.contador}")

objeto1 = Exemplo(10)
objeto2 = Exemplo(20)

objeto1.metodo_instancia()
objeto2.metodo_instancia()

Exemplo.metodo_classe()
