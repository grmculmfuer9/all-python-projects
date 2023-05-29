import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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
# fig.show()

"""Understand the Relationships in the Data
Run a Pair Plot
Challenge 6:

There might be some relationships in the data that we should know about. Before you run the code, make some predictions:

What would you expect the relationship to be between pollution (NOX) and the distance to employment (DIS)?
What kind of relationship do you expect between the number of rooms (RM) and the home value (PRICE)?
What about the amount of poverty in an area (LSTAT) and home prices?
Run a Seaborn .pairplot() to visualise all the relationships at the same time. 
Note, this is a big task and can take 1-2 minutes! After it's finished check your intuition 
regarding the questions above on the pairplot."""

# Challenge 6
print('Challenge 6')

ax = sns.pairplot(data=data, vars=['NOX', 'DIS'], height=9, aspect=0.7)
ax.fig.suptitle('Pollution vs Distance to Employment', fontsize=10)

ax = sns.pairplot(data=data, vars=['RM', 'PRICE'], height=9, aspect=0.7)
ax.fig.suptitle('Number of Rooms vs Home Value', fontsize=10)

ax = sns.pairplot(data=data, vars=['LSTAT', 'PRICE'], height=9, aspect=0.7)
ax.fig.suptitle('Poverty vs Home Value', fontsize=10)

# plt.show()

"""Challenge 7:

Use Seaborn's .jointplot() to look at some of the relationships in more detail. Create a jointplot for:

DIS and NOX
INDUS vs NOX
LSTAT vs RM
LSTAT vs PRICE
RM vs PRICE
Try adding some opacity or alpha to the scatter plots using keyword arguments under joint_kws."""

# Challenge 7
print('Challenge 7')

sns.jointplot(data=data, x='DIS', y='NOX', alpha=0.5)
sns.jointplot(data=data, x='INDUS', y='NOX', alpha=0.5)
sns.jointplot(data=data, x='LSTAT', y='RM', alpha=0.5)
sns.jointplot(data=data, x='LSTAT', y='PRICE', alpha=0.5)
sns.jointplot(data=data, x='RM', y='PRICE', alpha=0.5)

# plt.show()

"""Number of Rooms versus Home Value
Challenge 8:

Compare RM (number of rooms) with PRICE using Seaborn's .jointplot(). 
You can probably guess how the number of rooms affects home prices. 😊"""

# Challenge 8
print('Challenge 8')

with sns.axes_style('whitegrid'):
    sns.jointplot(x=data.RM,
                  y=data.PRICE,
                  height=7,
                  color='darkblue',
                  joint_kws={'alpha': 0.5})

plt.show()

"""Split Training & Test Dataset
We can't use all 506 entries in our dataset to train our model. 
The reason is that we want to evaluate our model on data that it hasn't seen yet (i.e., out-of-sample data). 
That way we can get a better idea of its performance in the real world.
Challenge 9:
1.	Import the train_test_split() function from sklearn
2.	Create 4 subsets: X_train, X_test, y_train, y_test
3.	Split the training and testing data roughly 80/20.
4.	To get the same random split every time you run your notebook use random_state=10. 
This helps us get the same results every time and avoid confusion while we're learning.
Hint: Remember, your target is your home PRICE, and your features are all the other columns 
you'll use to predict the price."""

# Challenge 9
print('Challenge 9')

X = data.drop('PRICE', axis=1)
y = data['PRICE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# % of training set
train_pct = 100 * len(X_train) / len(X)
print(f'Training data is {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100 * X_test.shape[0] / X.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')

"""Multivariable Regression
In a previous lesson, we had a linear model with only a single feature (our movie budgets). 
This time we have a total of 13 features. Therefore, our Linear Regression model will have the following form:

PRI^CE=θ0+θ1RM+θ2NOX+θ3DIS+θ4CHAS...+θ13LSTAT

Run Your First Regression
Challenge

Use sklearn to run the regression on the training dataset. 
How high is the r-squared for the regression on the training data?"""

# Challenge 10
print('Challenge 10')

model = LinearRegression()

model.fit(X_train, y_train)
rsquared = model.score(X_train, y_train)

print(f'Training data r-squared: {rsquared:.2}')

"""Evaluate the Coefficients of the Model
Here we do a sense check on our regression coefficients. The first thing to look for is if the coefficients 
have the expected sign (positive or negative).

Challenge 11: Print out the coefficients (the thetas in the equation above) for the features. Hint: 
You'll see a nice table if you stick the coefficients in a DataFrame.

1.  We already saw that RM on its own had a positive relation to PRICE based on the scatter plot. 
Is RM's coefficient also positive?
2.  What is the sign on the LSAT coefficient? Does it match your intuition and the scatter plot above?
3.  Check the other coefficients. Do they have the expected sign?
4.  Based on the coefficients, how much more expensive is a room with 6 rooms compared to a room with 5 rooms? 
According to the model, what is the premium you would have to pay for an extra room?"""

# Challenge 11
print('Challenge 11')

coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)

"""Analyse the Estimated Values & Regression Residuals
The next step is to evaluate our regression. How good our regression is depends not only on the r-squared. 
It also depends on the residuals - the difference between the model's predictions ( y^i ) 
and the true values ( yi ) inside y_train.

predicted_values = regr.predict(X_train)
residuals = (y_train - predicted_values)
Challenge: Create two scatter plots.

The first plot should be actual values (y_train) against the predicted value values


The cyan line in the middle shows y_train against y_train. If the predictions had been 100% accurate then all the 
dots would be on this line. The further away the dots are from the line, the worse the prediction was. 
That makes the distance to the cyan line, you guessed it, our residuals 😊

The second plot should be the residuals against the predicted prices. """

# Challenge 12
print('Challenge 12')

predicted_values = model.predict(X_train)
residuals = (y_train - predicted_values)

print(predicted_values)
print(residuals)

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_values, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\\hat y_i$', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\\hat y _i$', fontsize=14)

# plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_values, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
plt.xlabel('Predicted Prices $\\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)

plt.show()

"""Challenge 13:

Calculate the mean and the skewness of the residuals.
Again, use Seaborn's .displot() to create a histogram and superimpose the Kernel Density Estimate (KDE)
Is the skewness different from zero? If so, by how much?
Is the mean different from zero?"""

# Challenge 13
print('Challenge 13')

# Residual Distribution Chart
resid_mean = round(residuals.mean(), 2)
resid_skew = round(residuals.skew(), 2)

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Residuals Skew ({resid_skew}) Mean ({resid_mean})')

# plt.show()

"""Data Transformations for a Better Fit
We have two options at this point:

Change our model entirely. Perhaps a linear model is not appropriate.
Transform our data to make it fit better with our linear model.
Let's try a data transformation approach.

Challenge 14:

Investigate if the target data['PRICE'] could be a suitable candidate for a log transformation.

1. Use Seaborn's .displot() to show a histogram and KDE of the price data.
2. Calculate the skew of that distribution.
3. Use NumPy's log() function to create a Series that has the log prices
4. Plot the log prices using Seaborn's .displot() and calculate the skew.
5. Which distribution has a skew that's closer to zero?"""

# Challenge 14
print('Challenge 14')

# Price Distribution Chart
tgt_skew = data['PRICE'].skew()
sns.displot(data['PRICE'], kde='kde', color='green')
plt.title(f'Normal Prices. Skew is {tgt_skew:.3}')

# plt.show()

# Log Price Distribution Chart
log_tgt = np.log(data['PRICE'])
log_skew = log_tgt.skew()
sns.displot(log_tgt, kde='kde', color='green')
plt.title(f'Log Prices. Skew is {log_skew:.3}')

# plt.show()

"""How does the log transformation work?
Using a log transformation does not affect every price equally. Large prices are affected more than smaller 
prices in the dataset. Here's how the prices are "compressed" by the log transformation:


We can see this when we plot the actual prices against the (transformed) log prices.

Regression using Log Prices
Using log prices instead, our model has changed to:

log(PRI^CE)=θ0+θ1RM+θ2NOX+θ3DIS+θ4CHAS+...+θ13LSTAT 

Challenge 15:

Use train_test_split() with the same random state as before to make the results comparable.
Run a second regression, but this time use the transformed target data.
What is the r-squared of the regression on the training data?
Have we improved the fit of our model compared to before based on this measure?"""

# Challenge 15
print('Challenge 15')

plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')

plt.show()

# Log Price Regression
new_target = np.log(data['PRICE'])  # Use log prices
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features,
                                                            new_target,
                                                            test_size=0.2,
                                                            random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)

log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')

"""Evaluating Coefficients with Log Prices
Challenge 16: Print out the coefficients of the new regression model.
1.	Do the coefficients still have the expected sign?
2.	Is being next to the river a positive based on the data?
3.	How does the quality of the schools affect property prices? What happens to prices as there are more students 
per teacher?
Hint: Use a DataFrame to make the output look pretty."""

# Challenge 16
print('Challenge 16')

df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
print(df_coef)

"""Regression with Log Prices & Residual Plots
Challenge 17:

Copy-paste the cell where you've created scatter plots of the actual versus the predicted home prices as well as 
the residuals versus the predicted values.
Add 2 more plots to the cell so that you can compare the regression outcomes with the log prices side by side.
Use indigo as the colour for the original regression and navy for the color using log prices."""

# Challenge 17
print('Challenge 17')

# Graph of Actual vs. Predicted Log Prices
plt.figure(dpi=150)
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices: $y _i$ vs $\\hat y_i$ (R-Squared {log_rsquared:.2})', fontsize=17)
plt.xlabel('Actual Log Prices $y _i$', fontsize=14)
plt.ylabel('Prediced Log Prices $\\hat y _i$', fontsize=14)
# plt.show()

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=150)
plt.scatter(x=y_train, y=predicted_values, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices: $y _i$ vs $\\hat y_i$ (R-Squared {rsquared:.3})', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\\hat y _i$', fontsize=14)
# plt.show()

# Residuals vs Predicted values (Log prices)
plt.figure(dpi=150)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=17)
plt.xlabel('Predicted Log Prices $\\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
# plt.show()

# Residuals vs Predicted values
plt.figure(dpi=150)
plt.scatter(x=predicted_values, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=17)
plt.xlabel('Predicted Prices $\\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

"""Challenge 18:

Calculate the mean and the skew for the residuals using log prices. Are the mean and skew closer to 0 for the 
regression using log prices?"""

# Challenge 18
print('Challenge 18')

print(f'Log Residuals Mean: {log_residuals.mean():.3}')
print(f'Log Residuals Skew: {log_residuals.skew():.3}')

"""Compare Out of Sample Performance
The real test is how our model performs on data that it has not "seen" yet. This is where our X_test comes in.

Challenge 19

Compare the r-squared of the two models on the test dataset. Which model does better? 
Is the r-squared higher or lower than for the training dataset? Why?"""

# Challenge 19
print('Challenge 19')

print(f'Original Model Test Data r-squared: {model.score(X_test, y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')

"""Predict a Property's Value using the Regression Coefficients
Our preferred model now has an equation that looks like this:

log(PRI^CE)=θ0+θ1RM+θ2NOX+θ3DIS+θ4CHAS+...+θ13LSTAT 

The average property has the mean value for all its characteristics:"""

# Starting Point: Average Values in the Dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)),
                              columns=features.columns)
print(property_stats)

"""Challenge 20

Predict how much the average property is worth using the stats above. What is the log price estimate and 
what is the dollar estimate? You'll have to reverse the log transformation with .exp() to find the dollar value."""

# Challenge 20
print('Challenge 20')

log_estimate = log_regr.predict(property_stats)
print(log_estimate)
log_estimate = log_estimate[0]
print(f'Log Estimate: {log_estimate:.3}')

dollar_estimate = np.e ** log_estimate * 1000
print(f'Price in Dollars: {dollar_estimate:.3}')

"""Challenge 21

Keeping the average values for CRIM, RAD, INDUS and others, value a property with the following characteristics:"""

# Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75)  # high
amount_of_poverty = data.LSTAT.quantile(q=0.25)  # low

# Solution
# Set Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Actual Dollar Values
dollar_est = np.e ** log_estimate * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')

print(X_train)
