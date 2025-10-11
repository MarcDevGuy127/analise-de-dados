import pandas as pd
# Lendo um arquivo CSV
df_csv = pd.read_csv('dados_clientes_sujos.csv')
print(df_csv.head())

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [25, 32, 29, 41],
    'Salário': [2500, 3200, 2900, 4100]
}

df = pd.DataFrame(dados)

# Visualizando os dados
print(df)