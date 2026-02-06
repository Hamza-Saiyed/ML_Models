import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('house.csv')
# print(df.head())
# print(df.info())
# print(df.describe())

# print(df.isnull().sum())
# print(df.corr())

X = df[['area','bedrooms','age']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train,y_train)

print("Accuracy: ",model.score(X_test,y_test))

input_data = pd.DataFrame({
    "area" : [3000],
    "bedrooms" : [5],
    "age" : [0]
})

pred = model.predict(input_data)[0]
print("Predicted price: ",pred)