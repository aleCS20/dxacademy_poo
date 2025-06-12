# criando e gerenciando classe produto

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def atualizar_preco(self, novo_preco):
        if novo_preco > 0.0:
            self.preco = novo_preco
            print(f"Preço do {self.nome} atualizado para R$ {self.preco:.2f}")
        else:
            print(f"O preço do produto não pode ser menor que zero!")

    def atualizar_quantidade(self, nova_qtde):
        if nova_qtde > 0:
            self.quantidade = nova_qtde
            print(f"A quantidade de {self.nome} foi atualizado para {self.quantidade}")
        else:
            print("A quantidade informada não pode ser menor que zero!")

if __name__ == "__main__":
    produto1 = Produto("Arroz", 4.99, 10)
    produto1.exibir_informacoes()

    produto1.atualizar_preco(5.50)
    produto1.atualizar_quantidade(12)

    produto1.exibir_informacoes()