import pandas as pd

# import numpy as np
# import seaborn as sns
# import plotly.express as px
# import matplotlib.pyplot as plt
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
