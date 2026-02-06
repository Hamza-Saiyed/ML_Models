import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('house.csv')
print("Database Loaded Successfully")
print(df.head())

X = df[['area','bedrooms','age']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print("Accuracy: ",acc)

input_data = pd.DataFrame({
    "area": [3000],
    "bedrooms": [3],
    "age": [8]
})

pred = model.predict(input_data)
print("Prediction: ",pred[0])


with open('house_model2.pkl',"wb") as f:
    pickle.dump(model, f)
    
print("Model Saved Successfully as house_model2.pkl")

