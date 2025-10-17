import pandas as pd
from unidecode import unidecode

# Lendo um arquivo CSV
df_csv = pd.read_csv('dados_clientes_sujos.csv') # le o arquivo .csv
print(df_csv.head()) # acessa cabecalho das tabelas

df_csv['nome'] = df_csv['nome'].apply(unidecode)#  remove acentos
df_csv.columns = df_csv.columns.str.strip() # remove espacos
df_csv['ativo'] = df_csv['ativo'].str.strip() # remove espacos da coluna ativo

df_csv['ativo'] = df_csv['ativo'].replace({
    'TRUE': True,
    'FALSE': False,
    'sim': True,
    'Sim': True,
    'SIM': True,
    'NAO': False,
    'Não': False,
    '1': True,
    '0': False
})

#df_csv['ativo'] = df_csv['ativo'].str.upper

#df_csv['categoria_cliente'] = df_csv['categoria_cliente'].apply(unidecode)



print(df_csv)