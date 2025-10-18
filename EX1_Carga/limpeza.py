import pandas as pd
from unidecode import unidecode

# Lendo um arquivo CSV
df_csv = pd.read_csv('dados_clientes_sujos.csv') # le o arquivo .csv
print(df_csv.head()) # acessa cabecalho das tabelas

df_csv['nome'] = df_csv['nome'].apply(unidecode) # remove acentos
df_csv.columns = df_csv.columns.str.strip() # remove espacos de todas as colunas

df_csv['ativo'] = df_csv['ativo'].str.strip() # remove espacos da coluna ativo

df_csv['ativo'] = df_csv['ativo'].replace({ # substitui e formata valores para True ou False
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

# Remover linha com pelo menos um valor nulo
# df_csv = df_csv.dropna()

# Remover colunas nulas
# df_csv = df_csv.dropna(axis=1)

# remove todas linhas e colunas nulas
df_csv = df_csv.dropna(how='all')

# Removendo linhas duplicadas inteiras
df_csv = df_csv.drop_duplicates()


# remove espacos da coluna email
df_csv['email'] = df_csv['email'].str.strip()

# formatando coluna email como letras minusculas
df_csv['email'] = df_csv['email'].str.lower()

# eliminando linhas com dominios de email diferentes destes:
df_csv = df_csv[df_csv['email'].str.contains(r'@(outlook\.com|gmail\.com|yahoo\.com\.br|hotmail\.com)$', case=False, na=False)]

# removendo parenteses
df_csv['telefone'] = df_csv['telefone'].str.replace(r'[()]', '', regex=True)

# remove espacos da coluna telefone
df_csv['telefone'] = df_csv['telefone'].str.strip()

# garante que a coluna telefone só seja numeros e nao string
# df_csv['telefone'] = df_csv['telefone'].astype('Int64')            # converte para número inteiro (aceita NaN)
df_csv['telefone'] = df_csv['telefone'].astype('Int64')


print(df_csv)
print(df_csv['telefone'])

df_csv['telefone'].dtype
