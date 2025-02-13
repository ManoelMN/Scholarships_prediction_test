import pandas as pd

# Carregar dataset
df = pd.read_csv("data/scholarships_cleaned.csv")

# Contar categorias em colunas categóricas
categorical_cols = ["Brand", "Material", "Size", "Laptop Compartment", "Waterproof", "Style", "Color"]
category_counts = {col: df[col].nunique() for col in categorical_cols}

# Resumo estatístico das colunas numéricas
numeric_summary = df.describe()

# Mostrar resultados
print("\n🔹 Quantidade de categorias por coluna categórica:")
print(category_counts)

print("\n🔹 Resumo estatístico das colunas numéricas:")
print(numeric_summary)
