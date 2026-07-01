import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("house_price_linear_regression.csv")
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())
df = df.drop_duplicates()
df = df.dropna()
df = df[(df["area"] >= 30) & (df["area"] <= 200)]
df = df[(df["price"] >= 50) & (df["price"] <= 380)]
plt.figure(figsize=(8, 5))
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()
X = df[["area"]]
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
random_state=42
model = LinearRegression()
model.fit(X_train, y_train)
w = model.coef_[0]
b = model.intercept_
print("w =", w)
print("b =", b)
y_pred = model.predict(X_test)
result = pd.DataFrame({
    "真实房价": y_test.values,
    "预测房价": y_pred
})
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
plt.figure(figsize=(8, 5))

plt.scatter(df["area"], df["price"], label="Real Data")

x_line = df[["area"]].sort_values(by="area")
y_line = model.predict(x_line)

plt.plot(x_line, y_line, label="Linear Regression Line")

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Linear Regression: Area Predicts Price")
plt.legend()
plt.show()
new_house = pd.DataFrame({
    "area": [100]
})
predicted_price = model.predict(new_house)
print(predicted_price[0])