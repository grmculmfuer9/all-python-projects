import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
# import seaborn as sns
import pycountry
import os
import sys

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']


def lookup_country(location):
    try:
        location = location.split(',')[-1].strip()
        return pycountry.countries.lookup(location).alpha_3
    except LookupError:
        return None


def year(date):
    # datetime_object = datetime.strptime(date, "%Y")
    return date.year


def month(date):
    # datetime_object = datetime.strptime(date, "%Y")
    return MONTHS[date.month - 1]


base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
print('base_path: ', os.path.join(base_path, 'mission_launches.csv'))
pd.options.display.float_format = '{:,.2f}'.format
df_data = pd.read_csv(os.path.join(base_path, 'mission_launches.csv'))
print(pycountry.countries)

# Preliminary Data Exploration
print(df_data.shape)
print(df_data.info())
print(df_data.columns)
print(df_data.isna().values.any())
print(df_data.duplicated().values.any())

# Data Cleaning - Check for Missing Values and Duplicates
print(df_data.isna().sum())
print(df_data.duplicated().sum())

# Data Cleaning - Drop Duplicates
df_data.drop_duplicates(inplace=True)

# Data Cleaning - Drop Columns
df_data.drop(columns=['Unnamed: 0'], inplace=True)

# Descriptive Statistics
print(df_data.describe())

# Number of Launches per Company
plt.figure(figsize=(8, 5), dpi=120)
df_data['Organisation'].value_counts().plot(kind='bar')
plt.subplots_adjust(bottom=0.35)
plt.show()

# Number of Active versus Retired Rockets
plt.figure(figsize=(8, 5), dpi=120)
df_data['Rocket_Status'].value_counts().plot(kind='bar')
plt.xticks(rotation=0)
plt.show()

# Distribution of Mission Status
plt.figure(figsize=(8, 5), dpi=120)
df_data['Mission_Status'].value_counts().plot(kind='bar')
plt.xticks(rotation=0)
plt.show()

# How Expensive are the Launches?

# Drop nan values from the column Price
histo_price = df_data.dropna(subset=['Price'])
histo_price.loc[:, 'Price'] = histo_price['Price'].astype(float)

plt.figure(figsize=(8, 5), dpi=120)
histo_price['Price'].plot(kind='hist', bins=20)
plt.xlabel('Price in Millions')
plt.ylabel('Values in Millions')
plt.xlim(0, 1000)
plt.show()

# Convert countries in Location to ISO3 in the column Country
df_data['Country'] = df_data['Location'].apply(lookup_country)

# Use a Choropleth Map to Show the Number of Launches by Country using px.choropleth
country_counts = df_data['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Country_Appear']

fig = px.choropleth(country_counts, locations='Country', color='Country',
                    scope='world', color_continuous_scale='matter',
                    title='Number of Launches by Country',
                    labels={'Country_Appear': 'Number of Launches'},
                    hover_data=['Country_Appear'])
fig.show()

# Create a Plotly Sunburst Chart of the countries, organisations, and mission status
# Filter out rows with None values
filtered_data = df_data.dropna(subset=['Country', 'Organisation', 'Mission_Status'])

fig = px.sunburst(filtered_data, path=['Country', 'Organisation', 'Mission_Status'],
                  title='Number of Launches by Country, Organisation, and Mission Status',
                  color='Country', color_discrete_sequence=px.colors.sequential.Plasma_r)
fig.show()

# Analyse the Total Amount of Money Spent by Organisation on Space Missions
# Organisation value_counts
money_spent_by_organizations = df_data.groupby('Organisation')['Price'].sum().reset_index()
# print(money_spent_by_organizations)

# Analyse the Amount of Money Spent by Organisation per Launch
money_spent_by_organizations['Total_Launches'] = df_data['Organisation'].value_counts().reset_index()['Organisation']
money_spent_by_organizations = money_spent_by_organizations[(money_spent_by_organizations['Total_Launches'] != 0) &
                                                            (money_spent_by_organizations['Price'] != 0.00)]
# print(money_spent_by_organizations)

# Make a column for the average price per launch
money_spent_by_organizations['Average_Price_Per_Launch'] = money_spent_by_organizations['Price'] / \
                                                           money_spent_by_organizations['Total_Launches']
print(money_spent_by_organizations)

# Chart the Number of Launches per Year
# Convert the Launch_Date column to datetime
df_data['Date'] = pd.to_datetime(df_data['Date'])

# Create a column for the year
# df_data['Year'] = df_data['Date'].apply(lambda x: x.year)
df_data['Year'] = df_data['Date'].apply(year)

# Chart the Number of Launches per Year
plt.figure(figsize=(8, 5), dpi=120)
df_data['Year'].value_counts().plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Number of Launches')
xtick_positions = range(len(df_data['Year'].value_counts()))
xtick_labels = df_data['Year'].value_counts().index.tolist()
plt.xticks(xtick_positions[::3], xtick_labels[::3], rotation=45)
plt.subplots_adjust(bottom=0.15)
plt.show()

# Chart the Number of Launches Month-on-Month until the Present
# Which month has seen the highest number of launches in all time? Superimpose a rolling average on the month on month
# time series chart.
# Create a column for the month
df_data['Month'] = df_data['Date'].apply(month)

# Chart the Number of Launches Month-on-Month until the Present
plt.figure(figsize=(8, 5), dpi=120)
df_data['Month'].value_counts().plot(kind='bar')
# # Apply a rolling average to the month on month time series chart
# df_data['Month'].value_counts().rolling(12).mean().plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Number of Launches')
# xtick_positions = range(len(df_data['Month'].value_counts()))
# xtick_labels = df_data['Month'].value_counts().index.tolist()
# plt.xticks(xtick_positions[::3], xtick_labels[::3], rotation=45)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.15)
plt.show()

# How has the Launch Price varied Over Time?
# Create a line chart that shows the average price of rocket launches over time
# Filter out rows with None values
filtered_data = df_data.dropna(subset=['Price'])

# Create a line chart that shows the average price of rocket launches over time
plt.figure(figsize=(8, 5), dpi=120)
filtered_data.groupby('Year')['Price'].mean().plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.show()

# plt.figure(figsize=(8, 5), dpi=120)
top_10_organizations = df_data['Organisation'].value_counts().sort_values(ascending=False).head(10)

top_10_organizations.plot(kind='bar')
print('entered')
print(top_10_organizations)
plt.xlabel('Organisation')
plt.ylabel('Number of Launches')
plt.subplots_adjust(bottom=0.32)
plt.show()

# Chart the Number of Launches over Time by the Top 10 Organisations.
# How has the dominance of launches changed over time between the different players?
# Create a line chart that shows the number of launches over time by the top 10 organisations
# Filter out rows with None values
filtered_data = df_data.dropna(subset=['Organisation'])
organization_values = top_10_organizations.index.to_list()
filtered_data_organization = filtered_data[filtered_data['Organisation'].isin(organization_values)]

# Create a line chart that shows the number of launches over time by the top 10 organisations
filtered_data_organization.groupby(['Year', 'Organisation'])['Organisation'].count().unstack().plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.show()

# Cold War Space Race: USA vs USSR
filtered_data_space_race = filtered_data[filtered_data['Organisation'].isin(['NASA', 'RVSN USSR'])]

# Create a line chart that shows the number of launches over time by the USA and the USSR
filtered_data_space_race.groupby(['Year', 'Organisation'])['Organisation'].count().unstack().plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.show()

# Create a Plotly Pie Chart comparing the total number of launches of the USSR and the USA
filtered_data_space_race['Organisation'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.show()

# Chart the Total Number of Mission Failures Year on Year
mission_fails = df_data[df_data['Mission_Status'] == 'Failure']['Year'].value_counts().sort_index()
mission_fails.plot(kind='bar', figsize=(8, 5))
plt.xlabel('Year')
plt.ylabel('Number of Mission Failures')
xtick_positions = range(len(mission_fails))
xtick_labels = mission_fails.index.tolist()
plt.xticks(xtick_positions[::3], xtick_labels[::3], rotation=45)
plt.show()

# Chart the Percentage of Failures over Time
# Filter out rows with None values
filtered_data = df_data.dropna(subset=['Mission_Status'])

# Create a line chart that shows the percentage of failures over time
plt.figure(figsize=(8, 5), dpi=120)
filtered_data.groupby('Year')['Mission_Status'].apply(lambda x: ((x == 'Failure').sum() / len(x)) * 100).plot(
    kind='line')
plt.xlabel('Year')
plt.ylabel('Percentage of Failures (%)')
plt.ylim(0, 100)
plt.show()

# For Every Year Show which Country was in the Lead in terms of Total Number of Launches up to and including 2020
launches_per_year = df_data['Year'].value_counts().sort_index()
launches_per_year.plot(kind='bar', figsize=(8, 5))
plt.xlabel('Year')
plt.ylabel('Number of Launches')
xtick_positions = range(len(df_data['Year'].value_counts()))
xtick_labels = df_data['Year'].value_counts().index.tolist()
xtick_labels.sort()
plt.xticks(xtick_positions[::3], xtick_labels[::3], rotation=45)
plt.subplots_adjust(bottom=0.15)
plt.show()

# Create a Year-on-Year Chart Showing the Organisation Doing the Most Number of Launches
filtered_data.groupby(['Year', 'Organisation'])['Organisation'].count().unstack().plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.show()
