# sistema simples de biblioteca

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso ")
        else:
            print(f"O livro {self.titulo} já se encontra emprestado ")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido ")
        else:
            print(f"O livro {self.titulo} se encontra disponível ")

    def mostrar_disponibilidade(self):
        if self.disponivel:
            status = "disponivel"
        else:
            status = "emprestado"
        print(f"O Livro de {self.titulo} de autor: {self.autor} está: {status}")

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        novo_livro = Livro(titulo, autor)
        self.livros.append(novo_livro)
        print(f"Livro: {titulo} de autor: {autor} foi adicionado a biblioteca ")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f"Livro {titulo} não encontra-se na biblioteca ")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolver()
                return
        print(f"Livro {titulo} não encontra-se na biblioteca")

    def mostrar_inventario(self):
        print("\n ====================== Acervo de livros da Biblioteca =================== ")
        for livro in self.livros:
            livro.mostrar_disponibilidade()
        print("=" * 60)

biblioteca = Biblioteca()

biblioteca.adicionar_livro("Algortimos e Logica com Python", "Alessandro Oliveira")
biblioteca.adicionar_livro("Linguagem de Programação JavaScript", "Renato Augusto")

biblioteca.mostrar_inventario()

biblioteca.emprestar_livro("Algortimos e Logica com Python")

biblioteca.mostrar_inventario()

biblioteca.devolver_livro("Algortimos e Logica com Python")

biblioteca.mostrar_inventario()




