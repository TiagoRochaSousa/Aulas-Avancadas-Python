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