import pandas as pd

class Dados:
    def __init__(self, dados) -> None:
        self._dados = pd.read_csv(dados, sep=';')

    @property
    def dados(self):
        return self._dados
        
    def ler_inicio(self, linhas = 5):
        return self.dados.head(linhas)
    
    def ler_final(self, linhas = 5):
        return self.dados.tail(linhas)
    
    def ler_tipo(self):
        return type(self.dados)
    
    def ler_colunas(self):
        return self.dados.columns
    
    def tipo_dado_cabecalho(self, cabecalho):
        return self.dados[cabecalho]
    
    def media_rendas(self, agrupador, valor_de_media):
        return self.dados.groupby(agrupador)[valor_de_media].mean().round(2)
    
    def percentagem_por_tipo(self):
        return self.dados.Tipo.value_counts(normalize=True)
    
    def mostrar_valores_nulos(self):
        return self.dados.isnull().sum()
    
    def remover_valores_nulos(self, novo_valor):
        return self.dados.fillna(novo_valor, inplace=True)
    
    def econtrar_valores_zero(self):
        return self.dados.query('Quartos == 0 | Valor == 0 | Area == 0 | Condominio == 0')
    
    def remover_valores_zero(self):
        registos_a_remover = self.dados.query('Quartos == 0 | Valor == 0 | Area == 0 | Condominio == 0').index
        return self.dados.drop(registos_a_remover, axis=0, inplace=True)
    
    def filtro_quartos(self, num_quartos):
        return self.dados['Quartos'] == num_quartos
    
    def filtro_aluguer(self, aluguer):
        return self.dados['Valor'] < aluguer
    
    def filtro_quarto_aluguer(self):
        filtro1 = self.dados['Quartos'] == 1
        filtro2 = self.dados['Valor'] < 500
        filtro_composto = filtro1 & filtro2
        return self.dados[filtro_composto]
    
    def filtro_quarto_aluguer_area(self):
        filtro1 = self.dados['Quartos'] >= 2
        filtro2 = self.dados['Valor'] < 750
        filtro3 = self.dados['Area'] > 70
        filtro_composto2 = filtro1 & filtro2 & filtro3
        return self.dados[filtro_composto2]

    def media(self):
        return self.dados.groupby('Tipo')['Valor'].mean().round(2)
    
    def guardar(self, nome_arquivo, metodo=None, separador=';'): #UTF-8-sig #separador
        # decidir o que guardar
        if metodo:
            df_para_guardar = metodo()
        else:
            df_para_guardar = self.dados
        #guardar o que foi decidido acima
        df_para_guardar.to_csv(nome_arquivo, index=False, sep=separador, encoding='UTF-8-sig')
        print(f'{nome_arquivo} GUARDADO COM SUCESSO')

    def despesas_mensais(self):
        self.dados['Despesas mensais'] = self.dados['Valor'] + self.dados['Condominio']
        return self.dados
    
 


