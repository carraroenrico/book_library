import json

def salvar_dados(biblioteca):
    """
    Save the library data to a JSON file.

    Args:
        biblioteca (list): List of dictionaries representing the books.

    Writes the data to 'biblioteca.json' with UTF-8 encoding and
    pretty-printed indentation.
    """
    with open("biblioteca.json", "w", encoding="utf-8") as arquivo:
        json.dump(biblioteca, arquivo, indent=4, ensure_ascii=False)
    print("Dados salvos com sucesso!")

def carregar_dados():
    """
    Load the library data from a JSON file.

    Returns:
        list: The list of books loaded from 'biblioteca.json'.
              Returns an empty list if the file does not exist.
    """
    try:
        with open("biblioteca.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return [] 
    
def adicionar_livro(biblioteca, titulo, autor, ano):
    """
    Add a new book to the library.

    Args:
        biblioteca (list): The list of books to update.
        titulo (str): Title of the book.
        autor (str): Author of the book.
        ano (str): Publication year of the book.

    Appends a new dictionary representing the book to the library list.
    """
    novo_livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
    }
    biblioteca.append(novo_livro)

def listar_livros(biblioteca):
    """
    Print the title and author of every book in the library.

    Args:
        biblioteca (list): The list of books to display.
    """
    for livro in biblioteca:
        print (f'Titulo: {livro['titulo']} | Autor: {livro['autor']}')

def buscar_autor(biblioteca, nome_autor):
    """
    Search and print all books written by a given author.

    Args:
        biblioteca (list): The list of books to search through.
        nome_autor (str): The name of the author to search for.

    Prints each matching book's title and year. If no book is found,
    prints a message indicating that.
    """
    print(f'Livros de {nome_autor}:')
    encontrou = False
    for livro in biblioteca:
        if livro['autor'] == nome_autor:
            print(f'{livro['titulo']} ({livro['ano']})')
            encontrou = True
    if not encontrou:
        print('Nenhum livro encontrado para este autor')

def ano_limite(biblioteca, ano):
    """
    Print all books published after a given year.

    Args:
        biblioteca (list): The list of books to filter.
        ano (int): The year used as the lower bound (exclusive).

    Iterates through the library and prints books whose 'ano' field
    is greater than the given year.
    """
    print('Livros selecionados apos o ano escolhido')
    for livro in biblioteca:
        if int(livro['ano']) > ano:
            print(f' Livros: {livro['titulo']} | Ano: {livro['ano']}')
        else:
            continue

def remover_livro(biblioteca, titulo_removedor):
    """
    Remove a book from the library by its title.

    Args:
        biblioteca (list): The list of books to update.
        titulo_removedor (str): The title of the book to remove.

    Removes the first book found with a matching title. If no match
    is found, the library remains unchanged.
    """
    print('Removendo livro')
    for livro in biblioteca:
        if livro['titulo'] == titulo_removedor:
            biblioteca.remove(livro)
            break

minha_biblioteca = carregar_dados()

while True:
    print('\n1. Adicionar | 2. Listar | 3. Buscar Autor | 4. Filtrar Ano | 5. Remover | 0. Sair')
    opcao = input('Escolha uma opcao: ')

    if opcao == '0':
        salvar_dados(minha_biblioteca)
        print('Saindo do programa...')
        break
    
    elif opcao == '1':
        print('Qual livro deseja adicionar? (Ex."Dom Casmurro", "Machado de Assis", 1899 )')
        titulo = input('Adicione o titulo: ').lower()
        autor = input('Adicione o autor: ').lower()
        ano = input('Adicione o ano: ')
        adicionar_livro(minha_biblioteca, titulo, autor, ano)
        print('Livro adicionado.')
    
    elif opcao == '2':
        print('Listando livros: ')
        listar_livros(minha_biblioteca)
        
    elif opcao == '3':
        print('Digite o nome do autor: ')
        nome_autor = input('').lower()
        buscar_autor(minha_biblioteca, nome_autor)
    
    elif opcao == '4':
        entrada_ano = input('Digite o ano a ser filtrado: ')
        try:
            ano_filtrar = int(entrada_ano)
            ano_limite(minha_biblioteca, ano_filtrar)
        except ValueError:
            print('Voce digitou letras.')
            continue
        
    elif opcao == '5':
        print('Digite o livro a ser removido: ')
        titulo_removedor = input('').lower()
        try:
            titulo_removedor_string = str(titulo_removedor)
        except:
            print('Voce digitou caracteres indevidos')
            continue
        remover_livro(minha_biblioteca, titulo_removedor)
        print('Livro removido com sucesso.')

    else:
        print('Comando invalido. Tente novamente.')
        continue