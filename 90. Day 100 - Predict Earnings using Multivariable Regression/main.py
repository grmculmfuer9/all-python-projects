import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.options.display.float_format = '{:,.2f}'.format
df_data = pd.read_csv('NLSY97_subset.csv')

""":Key Variables:  
  1. S           Years of schooling (highest grade completed as of 2011)
  2. EXP         Total out-of-school work experience (years) as of the 2011 interview.
  3. EARNINGS    Current hourly earnings in $ reported at the 2011 interview"""

# Preliminary Data Exploration
print(df_data.shape)
print(df_data.info())
print(df_data.columns)
print(df_data.isna().values.any())
print(df_data.duplicated().values.any())

# Data Cleaning
df_data = df_data.dropna()
df_data = df_data.drop_duplicates()

# Descriptive Statistics
print(df_data.describe())

# Convert ID, S, EXP, EARNINGS to numeric
df_data['ID'] = pd.to_numeric(df_data['ID'], errors='coerce')
df_data['S'] = pd.to_numeric(df_data['S'], errors='coerce')
df_data['EXP'] = pd.to_numeric(df_data['EXP'], errors='coerce')
df_data['EARNINGS'] = pd.to_numeric(df_data['EARNINGS'], errors='coerce')

# # Visualize the features
# sns.set(style='whitegrid')
# # Exclude column ID in pairplot
# sns.pairplot(df_data[['S', 'EXP', 'EARNINGS']])
# plt.subplots_adjust(top=0.9)
# plt.show()

# Split Training & Test Dataset
# We can't use all the entries in our dataset to train our model. Keep 20% of the data for later as a testing dataset
# (out-of-sample data).
features = df_data[['S', 'EXP']]
target = df_data['EARNINGS']
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2,
                                                    random_state=42)

# Simple Linear Regression
# Only use the years of schooling to predict earnings. Use sklearn to run the regression on the training dataset.
# How high is the r-squared for the regression on the training data?
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)
print('R-squared for training data:', linear_model.score(x_train, y_train))

# Use the model to predict earnings for the test dataset. How high is the r-squared for the regression on the test data?
print('R-squared for test data:', linear_model.score(x_test, y_test))

print('Co-efficients of the model:', linear_model.coef_)
print('Intercept of the model:', linear_model.intercept_)
print(f'Equation of the model: EARNINGS = {linear_model.coef_[0]:.2f} * S + {linear_model.coef_[1]:.2f} * EXP + '
      f'{linear_model.intercept_:.2f}')

"""Analyse the Estimated Values & Regression Residuals
How good our regression is also depends on the residuals - the difference between the model's predictions ( 𝑦̂ 𝑖 ) and 
the true values ( 𝑦𝑖 ) inside y_train. Do you see any patterns in the distribution of the residuals?"""
# # Distribution of Residuals
# plt.figure(figsize=(9, 7))
# plt.title('Distribution of Residuals')
# sns.histplot(linear_model.predict(x_train), label='Test', kde=True, color='red')
# sns.histplot(y_train, label='Train', kde=True, color='blue', alpha=0.5)
# plt.legend()
# plt.show()

"""Use Your Model to Make a Prediction
How much can someone with a bachelors degree (12 + 4) years of schooling and 5 years work experience expect 
to earn in 2011?"""
print(features.columns)
predict_earnings = pd.DataFrame({'S': [16], 'EXP': [5]})
print(f'Predicted earnings: ${linear_model.predict(predict_earnings)[0]:.2f}')
