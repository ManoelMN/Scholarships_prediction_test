import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Carregar dataset limpo
df = pd.read_csv('C:/Users/manez/Documents/Scholarchips_project/data/scholarships_cleaned.csv')

# Separar features (X) e target (y)
X = df.drop(columns=['Price'])
y = df['Price']

# Identificar colunas numéricas e categóricas
num_features = ['Compartments', 'Weight Capacity (kg)']
cat_features = ['Brand', 'Material', 'Size', 'Laptop Compartment', 'Waterproof', 'Style', 'Color']

# Pré-processamento: Normalização One-Hot Encoding
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
])

# Criar pipeline com RandomForest
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])