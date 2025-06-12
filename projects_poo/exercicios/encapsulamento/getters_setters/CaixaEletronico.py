# gerenciando um sistema de caixa eletronico
from datetime import datetime
import uuid

class Cliente:
    def __init__(self, cpf: str, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class Conta:
    def __init__(self, numero: str, saldo: float = 0.0):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @saldo.setter
    def saldo(self, saldo: float):
        self.__saldo = saldo

    def sacar(self, valor: float):
        if valor > self.__saldo:
            return "Saldo em conta insuficiente!"
        else:
            self.__saldo -= valor
            return f"Você sacou R$ {valor:.2f} de sua conta com sucesso!"

    def depositar(self, valor: float):
        self.__saldo += valor
        return f"Voce depositou R$ {valor:.2f} em sua conta com sucesso!"

    def transferir(self, conta_destino, valor: float):
        if valor > self.__saldo:
            return "Valor informado é insuficiente para transferência"
        else:
            self.__saldo -= valor
            conta_destino.__saldo += valor
            return (f"Transferência de R$ {valor:.2f} para a conta {conta_destino.__numero}"
                    f"realizada com sucesso!")

    def mostrar_saldo(self):
        return f"Seu saldo atual: R${self.__saldo:.2f}"

class Movimentacao:
    def __init__(self, cliente: Cliente, conta: Conta):
        self.__id = uuid.uuid4()
        self.__data = datetime.now().date()
        self.__hora = datetime.now().time()
        self.__cliente = cliente
        self.__conta = conta

    def operacao(self, tipo: str, valor: float = 0.0, conta_destino: Conta = None):
        if (tipo.lower() == "sacar"):
            return self.__conta.sacar(valor)
        elif (tipo.lower() == "depositar"):
            return self.__conta.depositar(valor)
        elif (tipo.lower() == "transferir" and conta_destino is not None):
            return self.__conta.transferir(conta_destino, valor)
        elif (tipo.lower() == "saldo"):
            return self.__conta.mostrar_saldo()
        else:
            return "Operação inválida."

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def hora(self):
        return self.__hora

    @property
    def cliente(self):
        return self.__cliente

    @property
    def conta(self):
        return self.__conta

if __name__ == '__main__':

    cliente1 = Cliente("123.456.789-00", "Alessandro Barbosa")
    cliente2 = Cliente("987.654.321-00", "Maria Souza")

    conta1 = Conta("0001", 1000.0)
    conta2 = Conta("0002", 500.0)

    mov1 = Movimentacao(cliente1, conta1)
    print(mov1.operacao("sacar", 200.0))
    print(mov1.operacao("saldo"))

    mov2 = Movimentacao(cliente2, conta2)
    print(mov2.operacao("depositar", 300.0))
    print(mov2.operacao("saldo"))

    print(mov1.operacao("transferir", 300.0, conta_destino=conta2))
    print(mov1.operacao("saldo"))
    print(mov2.operacao("saldo"))
