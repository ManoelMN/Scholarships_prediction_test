import pandas as pd
import sqlite3

# Carregar dados 
df = pd.read_csv('C:/Users/manez/Documents/Scholarchips_project/data/scholarships_raw.csv')

# Visualizar as primeiras linhas
print(df.head(20))

# Resumo estatistico
print(df.describe())

# Tratar valores ausentes:
# Para colunas categóricas, usamos o valor da moda
df['Brand'] = df['Brand'].fillna(df['Brand'].mode()[0])
df['Material'] = df['Material'].fillna(df['Material'].mode()[0])
df['Size'] = df['Size'].fillna(df['Size'].mode()[0])
df['Laptop Compartment'] = df['Laptop Compartment'].fillna(df['Laptop Compartment'].mode()[0])
df['Waterproof'] = df['Waterproof'].fillna(df['Waterproof'].mode()[0])
df['Style'] = df['Style'].fillna(df['Style'].mode()[0])
df['Color'] = df['Color'].fillna(df['Color'].mode()[0])

# Para colunas numéricas vou usar a mediana
df['Compartments'] = df['Compartments'].fillna(df['Compartments'].median())
df['Weight Capacity (kg)'] = df['Weight Capacity (kg)'].fillna(df['Weight Capacity (kg)'].median())
df['Price'] = df['Price'].fillna(df['Price'].median())

# Corrigir tipos de dados
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Compartments'] = pd.to_numeric(df['Compartments'], errors='coerce')
df['Weight Capacity (kg)'] = pd.to_numeric(df['Weight Capacity (kg)'], errors='coerce')

# Verificar valores ausentes após o preenchimento
print(df.isna().sum())

# Criar banco de dados SQLite e salvar os dados limpos
conn = sqlite3.connect('C:/Users/manez/Documents/Scholarchips_project/data/scholarships.db')
df.to_sql('scholarships', conn, if_exists='replace', index=False)
conn.close()

# Salvar dataset limpo
df.to_csv('C:/Users/manez/Documents/Scholarchips_project/data/scholarships_cleaned.csv', index=False)

print("ETL concluido com sucesso!")


