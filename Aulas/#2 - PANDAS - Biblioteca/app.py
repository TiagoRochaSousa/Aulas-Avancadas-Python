import pandas as pd

from Modelos.classes import Dados

def main():
    base_de_dados = ('C:\\Users\\sousa\\Desktop\\Tiago Sousa\\Aulas Python Avançado IEFP\\Aulas\\'
                     '#2 - PANDAS - Biblioteca\\imoveis.csv')

    analise = Dados(base_de_dados)

    print('-----LER TABELA COMPLETA-----')
    print(analise.dados)

    print('-----LER INICIO DA TABELA-----')
    print(analise.ler_inicio(15))

    print('-----LER FINAL DA TABELA-----')
    print(analise.ler_final(15))

    print('-----LER TIPO DE DADOS-----')
    print(analise.ler_tipo())

    print('-----LER COLUNAS-----')
    print(analise.ler_colunas())

    print('-----LER TIPO DADO CABEÇALHO-----')
    print(analise.tipo_dado_cabecalho('Quartos'))

    print('-----MÉDIA DE RENDAS POR TIPO DE IMOVEL-----')
    print(analise.media_rendas('Tipo', 'Valor'))

    print('-----VER PERCENTAGEM POR TIPO DE IMOVEL-----')
    print(analise.percentagem_por_tipo())
    
    print('-----MOSTRAR VALORES NULOS-----')
    print(analise.mostrar_valores_nulos())

    print('-----REMOVER/ALTERAR VALORES NULOS-----')
    analise.remover_valores_nulos(0)

    print('-----MOSTRAR VALORES NULOS-----')
    print(analise.mostrar_valores_nulos())

    print('-----ENCONTRAR IMOVEIS COM VALOR ZERO-----')
    print(analise.econtrar_valores_zero())

    print('-----REMOVER IMOVEIS COM VALORES A ZERO-----')
    print(analise.remover_valores_zero())

    print('-----ENCONTRAR IMOVEIS COM VALOR ZERO-----')
    print(analise.econtrar_valores_zero())

    print('-----FILTROS DE QUARTOS-----')
    print(analise.filtro_quartos(1))

    print('-----FILTROS DE ALUGUER-----')
    print(analise.filtro_aluguer(500))

    print('-----FILTRO QUARTO(igual a 1) E ALUGUER(superior a 500)-----')
    print(analise.filtro_quarto_aluguer())

    print('-----FILTRO POR QUARTO(pelo menos 2)/ALUGUER(inferior a 750)/AREA(superior a 70)-----')
    print(analise.filtro_quarto_aluguer_area())

    #analise.guardar('teste123.csv', metodo=analise.media, separador=';')

    print('-----CRIAR COLUNA DESPESAS MENSAIS-----')
    print(analise.despesas_mensais())

    print('-----CRIAR COLUNA DESPESAS ANUAIS-----')
    print()


if __name__ == '__main__':
    main()

