class Livro:
    def __init__(self, titulo, autor, ano) -> None:
        self._titulo = titulo  
        self._autor = autor    
        self._ano = ano    

    def __str__(self) -> str:
                return (f'---- LIVRO ----\n'
                f'TITULO: {self._titulo}\n'
                f'AUTOR: {self._autor}\n'
                f'ANO: {self._ano}\n')
    
    @property
    def titulo(self):
        return f'TITULO: {self._titulo}' if len(self._titulo) > 0 else 'O titulo não é valido'
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        
    @property
    def autor(self):
        return f'AUTOR: {self._autor}' if len(self._autor) > 0 else 'O autor não é valido'
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor
        
    @property
    def ano(self):
        return f'ANO: {self._ano}' if len(self._ano) == 4 and self._ano.isnumeric() else 'O ano não é valido'
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano


class Ebook(Livro):
     def __init__(self, titulo, autor, ano, tamanho = 0) -> None:
          super().__init__(titulo, autor, ano)
          self._tamanho = tamanho

     def __str__(self) -> str:
          return (f'---- LIVRO ----\n'
                f'TITULO: {self._titulo}\n'
                f'AUTOR: {self._autor}\n'
                f'ANO: {self._ano}\n'
                f'TAMANHO: {self._tamanho} MB')

     @property
     def tamanho(self):
          return 'Nenhum ficheiro disponivel' if self._tamanho == 0 else f'TAMANHO: {self._tamanho} MB'
     
     @tamanho.setter
     def tamanho(self, novo_tamanho):
          self._tamanho = novo_tamanho


class Biblioteca():
    def __init__(self) -> None:
        self._livros = []
    
    def adicionar_livro(self):
            while True:
                escolha = input('Quer armazenar um livro ou um Ebook? [L/E]: ').strip().upper()
                if escolha == 'L':
                    titulo = input('Digite o titulo do livro: ')
                    if len(titulo) == 0:
                         print('Titulo nao pode ser vazio')
                         titulo = input('DIgite o titulo novamente: ')
                    else:
                         titulo
                    autor = input('Digite o autor do livro: ')
                    if len(autor) == 0:
                         print('O Autor não pode ficar vazio')
                         autor = input('Digite novamente o autor: ')
                    else:
                         autor = autor
                    ano = input('Digite o ano do livro: ')
                    livro = Livro(titulo, autor, ano)
                    self._livros.append(livro)
                elif escolha == 'E':
                    titulo = input('Digite o titulo do livro: ')
                    if len(titulo) == 0:
                         print('Titulo nao pode ser vazio')
                         titulo = input('Digite o titulo novamente: ')
                    else:
                         titulo = titulo
                    autor = input('Digite o autor do livro: ')
                    if len(autor) == 0:
                         print('O autor não pode estar vazio')
                         autor = input('Digite novamente o autor: ')
                    else:
                         autor = autor
                    ano = input('Digite o ano do livro: ')
                    tamanho = input('Digite o tamanho do ebook: ')
                    livro_digital = Ebook(titulo, autor, ano, tamanho)
                    self._livros.append(livro_digital)
                    opcao = input('Deseja continuar a armazenar livros? [S/N]: ').upper().strip()
                    if opcao == 'N':
                        break

    def mostrar_livros(self):
        for livro in self._livros:
            print(livro)
            print()
