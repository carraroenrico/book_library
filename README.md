# Library Manager

A simple Python script to manage a book library, storing data in a JSON file (`biblioteca.json`).

## How it works

- **Storage**: The library is a list of dictionaries, each with `titulo`, `autor`, and `ano`. On start, `carregar_dados()` reads this list from `biblioteca.json` (or starts empty if the file doesn't exist). On exit, `salvar_dados()` writes the list back to the file.

- **Add**: `adicionar_livro()` appends a new book (dictionary) to the list in memory.

- **List**: `listar_livros()` loops through the list and prints each book's title and author.

- **Search by author**: `buscar_autor()` loops through the list, printing any book whose `autor` matches the given name; if nothing matches, it prints a "not found" message.

- **Filter by year**: `ano_limite()` loops through the list and prints books whose `ano` (converted to `int`) is greater than the given year.

- **Remove**: `remover_livro()` loops through the list looking for the first book with a matching title, removes it, and stops.

- **Main loop**: The program runs an infinite `while` loop showing a menu; user input selects which function to call. Choosing `0` saves the data and exits.
