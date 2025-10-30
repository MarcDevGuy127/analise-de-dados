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
    'yes': True,
    'YES': True,
    'Yes': True,
    'NAO': False,
    'no': False,
    'NO': False,
    'No': False,
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

# removendo parenteses
df_csv['telefone'] = df_csv['telefone'].str.replace(r'[()]', '', regex=True)

# remove espacos da coluna telefone
df_csv['telefone'] = df_csv['telefone'].str.strip()

# garante que a coluna telefone só seja numeros e nao string
# df_csv['telefone'] = df_csv['telefone'].astype('Int64')            # converte para número inteiro (aceita NaN)
#df_csv['telefone'] = df_csv['telefone'].astype('Int64')

# Remover apenas os espaços dentro de cada célula
df_csv["telefone"] = (
    df_csv["telefone"]
    .astype(str)
    .str.replace(" ", "")   # tira espaços
    .str.replace("-", "")   # tira traços
)

# Remover o prefixo +55 ou 55 do início do número
df_csv["telefone"] = df_csv["telefone"].str.replace(r"^\+?55", "", regex=True)

meses = {
    "Jan": "01",
    "Fev": "02",
    "Mar": "03",
    "Abr": "04",
    "Mai": "05",
    "Jun": "06",
    "Jul": "07",
    "Ago": "08",
    "Set": "09",
    "Out": "10",
    "Nov": "11",
    "Dez": "12",
    "Sep": "09", 
    "Apr": "04",
    "Aug": "08",
    "Oct": "10",
    "Dec": "12"
}

# Substituir os nomes dos meses por números
for mes, num in meses.items():
    df_csv["data_nascimento"] = df_csv["data_nascimento"].astype(str).str.replace(mes, f"/{num}/", regex=True)

# Corrigir separadores, se necessário
df_csv["data_nascimento"] = (
    df_csv["data_nascimento"]
    .str.replace("-", "/")
    .str.replace(" ", "")
)

# Função para inverter manualmente as datas
def inverter_data(data):
    partes = str(data).split("/")
    if len(partes) == 3:
        # Detecta se o formato é AAAA/MM/DD (ano vem primeiro)
        if len(partes[0]) == 4:
            ano, mes, dia = partes
            return f"{dia}/{mes}/{ano}"
        # Caso contrário, já está no formato DD/MM/AAAA
        else:
            dia, mes, ano = partes
            return f"{dia}/{mes}/{ano}"
    return data  # Se não tiver 3 partes, deixa como está

# Aplicar a função a toda a coluna
df_csv["data_nascimento"] = df_csv["data_nascimento"].apply(inverter_data)

df_csv['cidade'] = df_csv['cidade'].apply(unidecode) # remove acentos de cidade

df_csv['estado'] = df_csv['estado'].str.strip() # remove espacos da coluna estado
df_csv['estado'] = df_csv['estado'].apply(unidecode) # remove acentos de estado

# remover espaços e - dentro de cada célula
df_csv["cep"] = (
    df_csv["cep"]
    .astype(str)
    .str.replace(" ", "")   # tira espaços
    .str.replace("-", "")   # tira traços
)

# remover espaços e - dentro de cada célula
df_csv["renda_mensal"] = (
    df_csv["renda_mensal"]
    .astype(str)
    .str.replace(" ", "")   # tira espaços
    .str.replace("R$", "")   # tira R$
)

df_csv["valor_compra_mais_recente"] = (
    df_csv["valor_compra_mais_recente"]
    .astype(str)
    .str.replace(" ", "")   # tira espaços
    .str.replace("R$", "")   # tira R$
)

# Garantir que tudo é texto e remover espaços
df_csv["renda_mensal"] = df_csv["renda_mensal"].astype(str).str.strip()
df_csv["valor_compra_mais_recente"] = df_csv["valor_compra_mais_recente"].astype(str).str.strip()
# Substituir vírgula por ponto para poder converter em número
df_csv["renda_mensal"] = df_csv["renda_mensal"].str.replace(",", ".", regex=False)
df_csv["valor_compra_mais_recente"] = df_csv["valor_compra_mais_recente"].str.replace(",", ".", regex=False)
# Converter para número (float)
df_csv["renda_mensal"] = pd.to_numeric(df_csv["renda_mensal"], errors="coerce")
df_csv["valor_compra_mais_recente"] = pd.to_numeric(df_csv["valor_compra_mais_recente"], errors="coerce")
# Formatar novamente com vírgula e duas casas decimais
df_csv["renda_mensal"] = df_csv["renda_mensal"].map(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
df_csv["valor_compra_mais_recente"] = df_csv["valor_compra_mais_recente"].map(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))


meses = {
    "Jan": "01",
    "Fev": "02",
    "Mar": "03",
    "Abr": "04",
    "Mai": "05",
    "Jun": "06",
    "Jul": "07",
    "Ago": "08",
    "Set": "09",
    "Out": "10",
    "Nov": "11",
    "Dez": "12",
    "Sep": "09", 
    "Apr": "04",
    "Aug": "08",
    "Oct": "10",
    "Dec": "12"
}

# Substituir os nomes dos meses por números
for mes, num in meses.items():
    df_csv["data_compra_mais_recente"] = df_csv["data_compra_mais_recente"].astype(str).str.replace(mes, f"/{num}/", regex=True)

# Corrigir separadores, se necessário
df_csv["data_compra_mais_recente"] = (
    df_csv["data_compra_mais_recente"]
    .str.replace("-", "/")
    .str.replace(" ", "")
)

# Aplicar a função a toda a coluna
df_csv["data_compra_mais_recente"] = df_csv["data_compra_mais_recente"].apply(inverter_data)

# Garantir que tudo é texto e remover espaços
df_csv["renda_mensal"] = df_csv["renda_mensal"].astype(str).str.strip()
df_csv["valor_compra_mais_recente"] = df_csv["valor_compra_mais_recente"].astype(str).str.strip()

# Substituir vírgula por ponto para poder converter em número
df_csv["renda_mensal"] = df_csv["renda_mensal"].str.replace(",", ".", regex=False)
df_csv["valor_compra_mais_recente"] = df_csv["valor_compra_mais_recente"].str.replace(",", ".", regex=False)

# Converter para número (float)
df_csv["renda_mensal"] = pd.to_numeric(df_csv["renda_mensal"], errors="coerce")
df_csv["valor_compra_mais_recente"] = pd.to_numeric(df_csv["valor_compra_mais_recente"], errors="coerce")

# Formatar novamente com vírgula e duas casas decimais
df_csv["renda_mensal"] = df_csv["renda_mensal"].map(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
df_csv["valor_compra_mais_recente"] = df_csv["valor_compra_mais_recente"].map(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

df_csv['ativo'] = df_csv['ativo'].replace({ # substitui e formata valores para True ou False
    True: 'SIM',
    False: 'NAO'
})
print(df_csv.head())
#print(df_csv['valor_compra_mais_recente'])

#df_csv['valor_compra_mais_recente'].dtype


# Salvar o DataFrame formatado em um novo arquivo CSV
df_csv.to_csv("modelo_resultado_limpeza.csv", index=False, encoding="utf-8-sig")

print("The file modelo_resultado_limpeza.csv is updated!")