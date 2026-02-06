import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
df = pd.read_csv('Car/car.csv')

print(df)

X = df[["engine_size","weight","horsepower"]]
y = df["mileage"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2,random_state = 42)
model = RandomForestRegressor()
model.fit(X_train,y_train)

print("Car Mileage Model Accuracy: ",model.score(X_test,y_test))

pickle.dump(model,open("Car/car_model.pkl","wb"))
print("Model Saved Successfully: car_model.pkl")