import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Criar a pasta de figuras
figures_path = 'reports/figures'
os.makedirs(figures_path, exist_ok=True)

# Carregar o dataset limpo
df = pd.read_csv('C:/Users/manez/Documents/Scholarchips_project/data/scholarships_cleaned.csv')

# Estatísticas gerais
print(df.describe())

# Histograma do preço das bolsas
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=50, kde=True)
plt.title('Distribuição dos Preços das Bolsas')
plt.savefig(os.path.join(figures_path, 'histograma_precos.png'))
plt.show()

# Boxplot de Compartments
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Compartments'])
plt.title('Distribuição de Compartments')
plt.savefig(os.path.join(figures_path,'boxplot_compartments.png'))
plt.show()

# Matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Compartments', 'Weight Capacity (kg)', 'Price']].corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.savefig(os.path.join(figures_path,'matriz_correlacao.png'))
plt.show()