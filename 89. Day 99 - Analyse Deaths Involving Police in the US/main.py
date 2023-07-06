import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import pycountry
import seaborn as sns
import os

import sys


# Function to convert 2-digit codes to 3-digit codes
def convert_country_code(code):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.alpha_3
    except ValueError:
        return code
    except KeyError:
        return code


pd.options.display.float_format = '{:,.2f}'.format

base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

df_hh_income = pd.read_csv(os.path.join(base_path, 'Median_Household_Income_2015.csv'), encoding="windows-1252")
df_pct_poverty = pd.read_csv(os.path.join(base_path, 'Pct_People_Below_Poverty_Level.csv'), encoding="windows-1252")
df_pct_completed_hs = pd.read_csv(os.path.join(base_path, 'Pct_Over_25_Completed_High_School.csv'), encoding="windows-1252")
df_share_race_city = pd.read_csv(os.path.join(base_path, 'Share_of_Race_By_City.csv'), encoding="windows-1252")
df_fatalities = pd.read_csv(os.path.join(base_path, 'Deaths_by_Police_US.csv'), encoding="windows-1252")

print('Starting')

# Replace 0 with NaN in all columns and rows in all dataframes
df_hh_income = df_hh_income.fillna(0)
df_pct_poverty = df_pct_poverty.fillna(0)
df_pct_completed_hs = df_pct_completed_hs.fillna(0)
df_share_race_city = df_share_race_city.fillna(0)
df_fatalities = df_fatalities.fillna(0)

# Chart the Poverty Rate in each US State Create a bar chart that ranks the poverty rate from highest to lowest by US
# state. Which state has the highest poverty rate? Which state has the lowest poverty rate? Bar Plot

# Convert poverty_rate to a numeric type
df_pct_poverty['poverty_rate'] = pd.to_numeric(df_pct_poverty['poverty_rate'], errors='coerce')

# Create the bar chart using matplotlib.pyplot
plt.figure(figsize=(9, 7), dpi=130)
plt.bar(x=df_pct_poverty['Geographic Area'], height=df_pct_poverty['poverty_rate'])
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate by State')
plt.show()

# Create the bar chart using seaborn
plt.figure(figsize=(9, 7), dpi=130)
sns.barplot(x='Geographic Area', y='poverty_rate', data=df_pct_poverty)
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate by State')
plt.show()

# Create the bar chart using plotly
fig = px.bar(df_pct_poverty, x='Geographic Area', y='poverty_rate', title='Poverty Rate by State')
fig.show()

# Chart the High School Graduation Rate by US State Show the High School Graduation Rate in ascending order of US
# States. Which state has the lowest high school graduation rate? Which state has the highest?

# Convert percent_completed_hs to a numeric type
df_pct_completed_hs['percent_completed_hs'] = pd.to_numeric(df_pct_completed_hs['percent_completed_hs'],
                                                            errors='coerce')
# Order the dataframe using groupby on geographic area and percent_completed_hs
sorted_percent_complete_hs = df_pct_completed_hs.groupby('Geographic Area')['percent_completed_hs'].count().sort_values(
    ascending=True)

# Create the bar chart using matplotlib.pyplot
plt.figure(figsize=(9, 7), dpi=130)
plt.bar(x=sorted_percent_complete_hs.index, height=sorted_percent_complete_hs.values)
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('High School Graduation Rate')
plt.title('High School Graduation Rate by State')
plt.show()

# Create the bar chart using seaborn
plt.figure(figsize=(9, 7), dpi=130)
sns.barplot(x=sorted_percent_complete_hs.index, y=sorted_percent_complete_hs.values)
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('High School Graduation Rate')
plt.title('High School Graduation Rate by State')
plt.show()

# Create the bar chart using plotly
fig = px.bar(sorted_percent_complete_hs, x=sorted_percent_complete_hs.index, y=sorted_percent_complete_hs.values,
             title='High School Graduation Rate by State', color=sorted_percent_complete_hs.index)
fig.show()

# Visualise the Relationship between Poverty Rates and High School Graduation Rates
# Create a line chart with two y-axes to show if the rations of poverty and high school graduation move together or
# inversely. Which states have the highest and lowest rates of high school graduation? Which states have the highest
# and lowest rates of poverty?

# Create the line chart using seaborn
plt.figure(figsize=(9, 7), dpi=130)
sns.lineplot(x='Geographic Area', y='poverty_rate', data=df_pct_poverty, label='Poverty Rate')
sns.lineplot(x='Geographic Area', y='percent_completed_hs', data=df_pct_completed_hs,
             label='High School Graduation Rate')
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Rate')
plt.title('Poverty Rate vs High School Graduation Rate by State')
plt.show()

# make a table containing geographic area, poverty rate, and high school graduation rate
merge_poverty_hs = pd.merge(df_pct_poverty, df_pct_completed_hs, on=['Geographic Area', 'City'])

# Create the line chart using plotly
fig = px.line(df_pct_poverty, x='Geographic Area', y='poverty_rate',
              title='Poverty Rate vs High School Graduation Rate by State')
fig.add_scatter(x=df_pct_completed_hs['Geographic Area'],
                y=df_pct_completed_hs['percent_completed_hs'], mode='lines',
                name='High School Graduation Rate')
fig.show()

# Now use a Seaborn .jointplot() with a Kernel Density Estimate (KDE) and/or scatter plot to visualise the same
# relationship

# Create the joint plot
sns.jointplot(data=merge_poverty_hs, x='poverty_rate', y='percent_completed_hs', kind='kde')

# Set the axis labels and title
plt.xlabel('State')
plt.ylabel('Rate')
plt.suptitle('Poverty Rate vs High School Graduation Rate by State')

# Display the plot
plt.show()

# Seaborn's .lmplot() or .regplot() to show a linear regression between the poverty ratio and the high school
# graduation ratio.

# Create the lmplot using Seaborn
sns.lmplot(data=merge_poverty_hs, x='poverty_rate', y='percent_completed_hs', scatter={'alpha': 0.3},
           line_kws={'color': 'red'}, height=7, aspect=1.5)

# Set the axis labels and title
plt.xlabel('Poverty Rate')
plt.ylabel('High School Graduation Rate')
plt.title('Poverty Rate vs High School Graduation Rate by State')
plt.subplots_adjust(top=0.9)

# Display the plot
plt.show()

# Create a regplot using seaborn
plt.figure(figsize=(9, 7), dpi=130)
sns.regplot(data=merge_poverty_hs, x='poverty_rate', y='percent_completed_hs', scatter={'alpha': 0.7},
            line_kws={'color': 'red'})

# Set the axis labels and title
plt.xlabel('Poverty Rate')
plt.ylabel('High School Graduation Rate')
plt.title('Poverty Rate vs High School Graduation Rate by State')

# Display the plot
plt.show()

# Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State
# Convert share_white, share_black, share_native_american, share_asian, and share_hispanic to numeric types
df_share_race_city['share_white'] = pd.to_numeric(df_share_race_city['share_white'], errors='coerce')
df_share_race_city['share_black'] = pd.to_numeric(df_share_race_city['share_black'], errors='coerce')
df_share_race_city['share_native_american'] = pd.to_numeric(df_share_race_city['share_native_american'],
                                                            errors='coerce')
df_share_race_city['share_asian'] = pd.to_numeric(df_share_race_city['share_asian'], errors='coerce')
df_share_race_city['share_hispanic'] = pd.to_numeric(df_share_race_city['share_hispanic'], errors='coerce')

count_df_share_race_city = df_share_race_city['Geographic area'].value_counts()
white_percent = df_share_race_city.groupby('Geographic area')['share_white'].sum() / count_df_share_race_city
black_percent = df_share_race_city.groupby('Geographic area')['share_black'].sum() / count_df_share_race_city
native_american_percent = df_share_race_city.groupby('Geographic area')['share_native_american'].sum() / \
                          count_df_share_race_city
asian_percent = df_share_race_city.groupby('Geographic area')['share_asian'].sum() / count_df_share_race_city
hispanic_percent = df_share_race_city.groupby('Geographic area')['share_hispanic'].sum() / count_df_share_race_city

white_percent = white_percent.reset_index().rename(columns={'index': 'Geographic Area', 0: 'White'})
black_percent = black_percent.reset_index().rename(columns={0: 'Black'})
native_american_percent = native_american_percent.reset_index().rename(columns={0: 'Native American'})
asian_percent = asian_percent.reset_index().rename(columns={0: 'Asian'})
hispanic_percent = hispanic_percent.reset_index().rename(columns={0: 'Hispanic'})

series_list = [white_percent, black_percent, native_american_percent, asian_percent, hispanic_percent]
column_names = ['Geographic Area', 'White', 'Black', 'Native American', 'Asian', 'Hispanic']
merged_series = pd.concat(series_list, axis=1)
merged_series.drop(columns='index', inplace=True)

# Create the bar plot
plt.figure(figsize=(9, 7), dpi=130)

x = merged_series['Geographic Area']  # x-axis values

for col in column_names[1:]:
    y = merged_series[col]  # y-axis values for each ethnicity
    plt.bar(x, y, label=col, alpha=0.7)

# Set the axis labels and title
plt.xlabel('Geographic Area')
plt.ylabel('Percentage')
plt.title('Percentage by Ethnicity')
plt.legend()
plt.xticks(rotation=90)

# Display the plot
plt.show()

# Create Donut Chart by of People Killed by Race
df_fatalities['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False,
                                            pctdistance=1.12, labeldistance=1.1)

plt.axis('equal')
# View the plot
plt.tight_layout()
plt.show()

# Create a Chart Comparing the Total Number of Deaths of Men and Women
df_fatalities['gender'].value_counts().plot(kind='bar', rot=0, color=['blue', 'red'])

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Number of Deaths')

# Display the plot
plt.show()

# Create a Box Plot Showing the Age and Manner of Death
# Break out the data by gender using df_fatalities. Is there a difference between men and women in the manner of death?

# Convert age column to numeric
df_fatalities['age'] = pd.to_numeric(df_fatalities['age'], errors='coerce')

# Create the box plot
plt.figure(figsize=(9, 7), dpi=130)
fig = px.box(df_fatalities, x='age', y='manner_of_death', notched=True,
             points='all', hover_data=df_fatalities.columns)
fig.show()

# Were People Armed or Unarmed?
df_fatalities['armed'].value_counts()[:5].plot(kind='bar', rot=0, color=['blue', 'red', 'green', 'purple', 'orange'])

# Add labels and title
plt.xlabel('Armed')
plt.ylabel('Number of Deaths')

# Display the plot
plt.show()

# How Old Were the People Killed?

# Create a histogram and KDE plot that shows the distribution of ages of the people killed by police
plt.figure(figsize=(9, 7), dpi=130)
df_fatalities['age'].plot(kind='hist', bins=40, density=True, alpha=0.7)
df_fatalities['age'].plot(kind='kde')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Number of Deaths')
plt.title('Age Distribution of People Killed by Police')
plt.xlim(0, 100)

# Display the plot
plt.show()

# Create a separate KDE plot for each race. Is there a difference between the distributions?
plt.figure(figsize=(9, 7), dpi=130)
df_fatalities['race'].value_counts().plot(kind='bar', rot=0)

# Add labels and title
plt.xlabel('Race')
plt.ylabel('Number of Deaths')

# Display the plot
plt.show()

# Mental Illness and Police Killings
# What percentage of people killed by police have been diagnosed with a mental illness?

# Plot a bar chart
df_fatalities['signs_of_mental_illness'].value_counts().plot(kind='pie', rot=0, autopct='%1.1f%%',
                                                             shadow=False, pctdistance=0.50, labeldistance=1.05)

# Add labels and title
plt.xlabel('Signs of Mental Illness')
plt.ylabel('Number of Deaths')

# Display the plot
plt.show()

# In Which Cities Do the Most Police Killings Take Place?
# Create a chart ranking the top 10 cities with the most police killings. Which cities are the most dangerous?

# Plot a bar chart
df_fatalities['city'].value_counts()[:10].plot(kind='bar', rot=45)

# Add labels and title
plt.xlabel('City')
plt.ylabel('Number of Deaths')
plt.subplots_adjust(bottom=0.25)

# Display the plot
plt.show()

# Rate of Death by Race Find the share of each race in the top 10 cities. Contrast this with the top 10 cities of
# police killings to work out the rate at which people are killed by race for each city.

# Create a new dataframe with the top 10 cities
top_ten_cities = df_fatalities[['city', 'race']].value_counts()[:10].reset_index(name='count')

# Plot the bar chart using seaborn
plt.figure(figsize=(9, 7), dpi=130)
sns.barplot(top_ten_cities, x='city', y='count', hue='race', palette='bright')

# Add labels and title
plt.xlabel('City')
plt.ylabel('Number of Deaths')
plt.legend(loc='upper right')

# Display the plot
plt.show()

# Create a Choropleth Map of Police Killings by US State Which states are the most dangerous? Compare your map with
# your previous chart. Are these the same states with high degrees of poverty?

# Create a new dataframe with the total number of people killed by state
state_kills = df_fatalities['state'].value_counts().reset_index(name='count')
state_kills['index'] = state_kills['index'].apply(convert_country_code)

# Create the map
fig = px.choropleth(state_kills, locations='index', color='count', color_continuous_scale='Viridis',
                    hover_name='index', locationmode='USA-states', scope='usa', labels={'count': 'Number of Deaths'})
fig2 = px.choropleth(state_kills, locations='index', color='count', color_continuous_scale='Viridis',
                     hover_name='index', labels={'count': 'Number of Deaths'})
fig.show()
fig2.show()

# Number of Police Killings Over Time
# Analyse the Number of Police Killings over Time. Is there a trend in the data?
df_fatalities['date'] = pd.to_datetime(df_fatalities['date'])
df_fatalities['year'] = df_fatalities['date'].dt.year

# Plot the number of police killings per year
plt.figure(figsize=(9, 7), dpi=130)
df_fatalities['year'].value_counts().plot(kind='bar', rot=0, color=['blue', 'red', 'green', 'purple', 'orange'],
                                          width=0.5, align='center', alpha=0.7, label='Deaths by Year')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Deaths')

# Display the plot
plt.show()
