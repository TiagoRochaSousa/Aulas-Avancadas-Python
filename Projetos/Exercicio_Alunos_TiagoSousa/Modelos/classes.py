import pandas as pd

class Aluno:
    def __init__(self, dados) -> None:
        self._dados = pd.read_csv(dados, sep=',')

    @property
    def dados(self):
        return self._dados

    def ler_inicio(self):
        return self._dados.head(15)

    def media_alunos(self):
        self.dados['Media'] = (self.dados['Exercício 1'] + self.dados['Exercício 2'] + self.dados['Exercício 3'] + self.dados['Exercício 4'] + self.dados['Exercício 5']) / 5
        return self.dados
    
    def situacao(self):
        self.dados['Situacao'] = 'Reprovado'
        self.dados['Situacao'][self.dados['Media'] >= 9.5] = 'Aprovado'
        return self.dados
    
    def criar_ficheiro_aprovado(self, nome_arquivo, separador = ','):
        aprovados = self.dados[self.dados['Situacao'] == 'Aprovado']
        aprovados.to_csv(nome_arquivo, index=False, sep = separador, encoding='UTF-8-sig')

    def criar_ficheiro_reprovado(self, nome_arquivo, separador = ','):
        reprovados = self.dados[self.dados['Situacao'] == 'Reprovado']
        reprovados.to_csv(nome_arquivo, index=False, sep = separador, encoding='UTF-8-sig')

    def guardar_nova_coluna(self, nome_arquivo, separador = ','):
        self.dados['Media'] = (self.dados['Exercício 1'] + self.dados['Exercício 2'] + self.dados['Exercício 3'] + self.dados['Exercício 4'] + self.dados['Exercício 5']) / 5
        self.dados.to_csv(nome_arquivo, index=False, sep = separador, encoding='UTF-8-sig')
        return self.dados

