import pandas as pd

from Modelos.classes import Aluno

def main():
    base_de_dados = ('C:\\Users\\sousa\\Desktop\\Tiago Sousa\\Aulas Python Avançado IEFP\\'
                     'Projetos\\Exercicio_Alunos_TiagoSousa\\Alunos_Exercicios.csv')

    analise = Aluno(base_de_dados)

    print(analise.dados)
    print(analise.ler_inicio())

    print('---------------Média dos alunos---------------')
    print(analise.media_alunos())

    print('---------------SITUAÇÃO---------------')
    print(analise.situacao())

    print('---------------CRIAR FICHEIRO APROVADOS---------------')
    print(analise.criar_ficheiro_aprovado('Arquivo Aprovados.csv', separador=','))

    print('---------------CRIAR FICHEIRO REPROVADOS---------------')
    print(analise.criar_ficheiro_reprovado('Arquivo Reprovados.csv', separador=','))

    analise.guardar_nova_coluna('Tabela completa.csv', separador=',')

if __name__ == '__main__':
    main()


