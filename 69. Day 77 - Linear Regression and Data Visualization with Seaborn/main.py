import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()
data = pd.read_csv('cost_revenue_dirty.csv')

# Exploring and cleaning the data
print(data.shape)
print(data.isna().values.any())
print(data.isna().values.sum())
print(data.duplicated().values.any())
columns = data.columns

for x in columns[-3:]:
    # Convert to float
    data[x] = data[x].str.replace('$', '').str.replace(',', '').astype(float)
    print(data[x][0], type(data[x][0]))

data['Release_Date'] = pd.to_datetime(data['Release_Date'])
print(data.info())

for x in columns:
    # Check data types
    print(x + ": ", type(data[x][0]))

# Exploring the data
print(data.describe())

# How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that
# grossed nothing?
# &
# How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally (i.e.,
# the biggest flops)?
print(data[data.USD_Domestic_Gross == 0].count())
print(data.loc[(data.USD_Domestic_Gross == 0) & (data.USD_Worldwide_Gross == 0)].sort_values(
    'USD_Production_Budget',
    ascending=False).Movie_Title)

scrape_data = pd.Timestamp('2018-05-01')
data_clean = data.loc[
    (data.USD_Domestic_Gross != 0) & (data.USD_Worldwide_Gross != 0)]

decade_column = data_clean.Release_Date.dt.year // 10 * 10
data_clean.insert(loc=len(columns), column='Decade', value=pd.to_datetime(decade_column))
old_films = data_clean[data_clean.Decade < pd.Timestamp(1970)]
new_films = data_clean[data_clean.Decade >= pd.Timestamp(1970)]

# Seaborn and Matplotlib Visualization
plt.figure(figsize=(8, 4), dpi=130)

# set styling on a single chart
with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data=data_clean,
                         x='USD_Production_Budget',
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

# plt.show()

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross', )

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

plt.figure(figsize=(8, 4), dpi=130)
with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})

plt.figure(figsize=(8, 4), dpi=130)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.4},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

# plt.show()

# Linear Regression
regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
x = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

regression.fit(x, y)
print(regression.intercept_)
print(regression.coef_)
print(regression.score(x, y))

# Explanatory Variable(s) or Feature(s)
x = pd.DataFrame(old_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])

regression.fit(x, y)
print(regression.intercept_)
print(regression.coef_)
print(regression.score(x, y))

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0, 0] * budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}')
