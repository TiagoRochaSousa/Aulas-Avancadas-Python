from Classe.classes import Livro


print('------Digite o seu livro------')
print()
titulo = input('Digite o titulo do livro: ')
autor = input('Digite o autor do livro: ')
ano = input('Digite o ano do livro: ')

livro = Livro(titulo, autor, ano)


print(livro.titulo)
print(livro.autor)
print(livro.ano)
