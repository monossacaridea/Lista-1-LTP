# Exercício 6: Crie um programa que gerencie o banco de dados de uma biblioteca. O programa deve permitir adicionar um novo livro (como uma lista contendo título, autor e ano), listar todos os livros, e permitir a busca de livros pelo título.

biblioteca = []

def adicionar_livro(titulo, autor, ano):
    livro = {'titulo': titulo, 'autor': autor, 'ano': ano}
    biblioteca.append(livro)
    print(f"O livro '{titulo}' foi adicionado com sucesso!")

def listar_livros():
    if len(biblioteca) == 0:
        print("A biblioteca está vazia.")
    else:
        print("\nLista de livros:")
        for idx, livro in enumerate(biblioteca, start=1):
            print(f"{idx}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    print()

def buscar_livro(titulo_busca):
    resultados = [livro for livro in biblioteca if titulo_busca.lower() in livro['titulo'].lower()]

    if resultados:
        print("\nResultados da busca:")
        for livro in resultados:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print(f"Nenhum livro encontrado com o título '{titulo_busca}'.")
    print()

def menu():
    while True:
        print("1. Adicionar um novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro pelo título")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano do livro: ")
            adicionar_livro(titulo, autor, ano)
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            titulo_busca = input("Digite o título do livro que deseja buscar: ")
            buscar_livro(titulo_busca)
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
