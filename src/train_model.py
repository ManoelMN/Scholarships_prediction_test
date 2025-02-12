import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from model import model_pipeline # Importa o pipeline criado em model.py

# Carregar dataset
df = pd.read_csv('C:/Users/manez/Documents/Scholarchips_project/data/scholarships_cleaned.csv')

# Separar features e target
X = df.drop(columns=['Price'])
y = df['Price']

# Dividir dados em treinos e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model_pipeline.fit(X_train, y_train)

# Fazer previsões
y_pred = model_pipeline.predict(X_test)

# Avaliação do modelo
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.2f}")

# Salvar modelo treinado
joblib.dump(model_pipeline, "src/random_forest_model.pkl")

# Criar um DataFrame com valores reais e preditos
df_results = X_test.copy()
df_results['Actual Price'] = y_test.values
df_results['Predicted Price'] = y_pred

# Garantir que os valores numericos estejam corretos
df_results["Actual Price"] = pd.to_numeric(df_results['Actual Price'], errors='coerce').round(2)
df_results["Predicted Price"] = pd.to_numeric(df_results['Predicted Price'], errors='coerce').round(2)
df_results["Weight Capacity (kg)"] = pd.to_numeric(df_results['Weight Capacity (kg)'], errors='coerce').round(2)
df_results["Compartments"] = pd.to_numeric(df_results['Compartments'], errors='coerce').astype(int)

# Salvar como CSV para importar no Power Bi
df_results.to_csv("data/model_predictions.csv", sep=";", decimal=",", index=False)