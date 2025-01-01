

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import datetime as dt

df = pd.read_csv('uber.csv')

df.head()

df.info()

df.isna().sum()

df.dropna(inplace = True)

df.isna().sum()

df.drop(["Unnamed: 0", "key"], axis = 1, inplace = True)

df.describe()

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

df.info()

# Visualize the Outliers for fare_amount
import matplotlib.pyplot as plt
plt.boxplot(df["fare_amount"])

def find_outliers(df):
    q1 = df.quantile(0.25) 
    q3 = df.quantile(0.75) 
    IQR = q3-q1 
    outliers = df[(df<q1-1.5*IQR) | (df>q3+1.5*IQR)]
    return outliers

# Outlier Insights
fare_amount_outliers = find_outliers(df["fare_amount"])
print("Number of Outlier : " + str(len(fare_amount_outliers)))
print("Max Outlier : " + str(fare_amount_outliers.max()))
print("Min Outlier : " + str(fare_amount_outliers.min()))

# Droping Outliers
q_low = df["fare_amount"].quantile(0.25)
q_hi  = df["fare_amount"].quantile(0.75)
iqr = q_hi - q_low
df = df[(df["fare_amount"] < q_hi+1.5*iqr) & (df["fare_amount"] > q_low-1.5*iqr)]

df.drop(df[df['fare_amount'] < 0].index, inplace = True)

# Co-relation Heatmap
import seaborn as sns
sns.heatmap(df.corr(), annot = True)

df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
df['month'] = df['pickup_datetime'].dt.month

def haversine(lon1, lat1, lon2, lat2):
    R = 6371  # Radius of earth in kilometers
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(delta_lambda/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))

    return R * c  

df['distance_km'] = haversine(df['pickup_longitude'], df['pickup_latitude'],
                              df['dropoff_longitude'], df['dropoff_latitude'])

df.drop(['pickup_datetime'], axis=1, inplace=True)

X = df[['distance_km', 'hour', 'day_of_week', 'month', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']]
y = df['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)

y_pred_linear = linear_model.predict(X_test_scaled)

r2_linear = r2_score(y_test, y_pred_linear)
rmse_linear = np.sqrt(mean_squared_error(y_test, y_pred_linear))

print("Linear Regression R²:", r2_linear)
print("Linear Regression RMSE:", rmse_linear)

# Random Forest Regression Model
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)

y_pred_rf = random_forest_model.predict(X_test)

r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

print("Random Forest Regression R²:", r2_rf)
print("Random Forest Regression RMSE:", rmse_rf)

# Comparing the results
results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R² Score": [r2_linear, r2_rf],
    "RMSE": [rmse_linear, rmse_rf]
})
print(results)

# Plotting results
plt.figure(figsize=(10, 6))
sns.barplot(x="Model", y="RMSE", data=results)
plt.title('RMSE Comparison between Models')
plt.show()