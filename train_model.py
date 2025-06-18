
# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample training data
data = {
    'size': [1000, 1500, 2000, 2500, 3000],
    'bed': [2, 3, 3, 4, 4],
    'bath': [1, 2, 2, 3, 3],
    'age': [10, 5, 20, 15, 10],
    'price': [50_00_000, 75_00_000, 95_00_000, 1_15_00_000, 1_30_00_000]
}

df = pd.DataFrame(data)

X = df[['size', 'bed', 'bath', 'age']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as 'model.pkl'")




