import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.markdown(""" 
            ## Simple Linear Regression
            - Predict medium house value
            """)

# Load the dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

st.text(df.head())
st.text(df.describe())

X = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']]
y = df['MedHouseVal']

st.code("""
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)        
""")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
st.text(f'Mean Squared Error: {mse}')

# enable dark mode
plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.set_xlabel('Actual Values')
ax.set_ylabel('Predicted Values')
ax.set_title('Actual vs Predicted Values')

st.pyplot(fig)

st.markdown("""
            References  
            [California housing dataset](https://inria.github.io/scikit-learn-mooc/python_scripts/datasets_california_housing.html#:~:text=In%20this%20dataset,%20we%20have%20information)   
            """)

 
