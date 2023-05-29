import pandas as pd
import plotly.express as px
import seaborn as sns

# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.linear_model import LinearRegression

# TODO: Add missing import statements

pd.options.display.float_format = '{:,.2f}'.format

data = pd.read_csv('boston.csv', index_col=0)

"""Understand the Boston House Price Dataset
Characteristics:

:Number of Instances: 506 

:Number of Attributes: 13 numeric/categorical predictive. The Median Value (attribute 14) is the target.

:Attribute Information (in order):
    1. CRIM     per capita crime rate by town
    2. ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
    3. INDUS    proportion of non-retail business acres per town
    4. CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    5. NOX      nitric oxides concentration (parts per 10 million)
    6. RM       average number of rooms per dwelling
    7. AGE      proportion of owner-occupied units built prior to 1940
    8. DIS      weighted distances to five Boston employment centres
    9. RAD      index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
    13. LSTAT    % lower status of the population
    14. PRICE     Median value of owner-occupied homes in $1000's

:Missing Attribute Values: None

:Creator: Harrison, D. and Rubinfeld, D.L."""

"""Challenge 1:
1.	What is the shape of data?
2.	How many rows and columns does it have?
3.	What are the column names?
4.	Are there any NaN values or duplicates?"""

# Challenge 1
print('Challenge 1')
print(data.shape)
print(data.describe())
print(data.columns)
print(data.isna().values.any())
print(data.duplicated().values.any())

"""Challenge 2: Data Cleaning - Check for Missing Values and Duplicates"""

# Challenge 2
print('Challenge 2')
# Done

"""Challenge 3:
1.	How many students are there per teacher on average?
2.	What is the average price of a home in the dataset?
3.	What is the CHAS feature?
4.	What are the minimum and the maximum value of the CHAS and why?
5.	What is the maximum and the minimum number of rooms per dwelling in the dataset?"""

# Challenge 3
print('Challenge 3')
print(data['PTRATIO'].mean())
print(data['PRICE'].mean())
print(data['CHAS'].describe())
print(data['CHAS'].min())
print(data['CHAS'].max())
print(data['RM'].min())
print(data['RM'].max())

"""Visualise the Features
Challenge 4: Having looked at some descriptive statistics, visualise the data for your model. 
Use Seaborn's .displot() to create a bar chart and superimpose the Kernel Density Estimate (KDE) 
for the following variables:

1.	PRICE: The home price in thousands.
2.	RM: the average number of rooms per owner unit.
3.	DIS: the weighted distance to the 5 Boston employment centres i.e., the estimated length of the commute.
4.	RAD: the index of accessibility to highways.
Try setting the aspect parameter to 2 for a better picture.

What do you notice in the distributions of the data?"""

# Challenge 4
print('Challenge 4')

# House Prices 💰
sns.displot(data['PRICE'], kde=True, aspect=2)

# Number of Rooms 🛏️
sns.displot(data['RM'], kde=True, aspect=2)

# Distance to Employment - Length of Commute 🚗
sns.displot(data['DIS'], kde=True, aspect=2)

# Access to Highways 🛣
sns.displot(data['RAD'], kde=True, aspect=2)

# plt.show()

"""Next to the River? ⛵️
Challenge 5:

Create a bar chart with plotly for CHAS to show many more homes are away from the river versus next to it. 
You can make your life easier by providing a list of values for the x-axis (e.g., x=['No', 'Yes'])"""

# Challenge 5
print('Challenge 5')

count_homes_near_river = data['CHAS'].value_counts()
print(count_homes_near_river)

fig = px.bar(count_homes_near_river, x=['No', 'Yes'], y=count_homes_near_river.values, color='CHAS')
fig.update_layout(xaxis_title='Property located next to the river',
                  yaxis_title='Number of Homes',
                  xaxis={'categoryorder': 'total descending'})
fig.show()
