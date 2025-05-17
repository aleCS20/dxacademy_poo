#exemplo Conta Bancária com encapsulamento

class ContaBancaria:
    taxa_juros = 0.02

    def __init__(self, titular, saldo):
        # atributos privados
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
        else:
            print(f"O valor do depósito deve ser positivo")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            print(f"Saque de R$ {valor:.2f} realizado com sucesso")
        else:
            print(f"Saldo insuficiente ou valor de saque inválido")

    def mostrar_saldo(self):
        print(f"Saldo de {self.__titular} - R$ {self.__saldo:.2f}")

    @classmethod
    def conta_com_juros(cls, titular, saldo_inicial):
        saldo_com_juros = saldo_inicial * (1 + cls.taxa_juros)
        return cls(titular, saldo_com_juros)

conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria.conta_com_juros("Bob", 1000)

conta1.mostrar_saldo()
conta1.depositar(200)
conta1.sacar(150)
conta1.mostrar_saldo()
print("############################################")
conta2.mostrar_saldo()
conta2.depositar(500)
conta2.sacar(300)
conta2.mostrar_saldo()