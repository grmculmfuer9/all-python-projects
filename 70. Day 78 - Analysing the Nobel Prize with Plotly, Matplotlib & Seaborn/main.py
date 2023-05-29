import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns

# from statsmodels.nonparametric.smoothers_lowess import lowess

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('nobel_prize_data.csv')

"""Challenge 1
Preliminary data exploration.

What is the shape of df_data? How many rows and columns?

What are the column names and what kind of data is inside of them?

In which year was the Nobel prize first awarded?

Which year is the latest year included in the dataset?

Challenge 2
Are there any duplicate values in the dataset?

Are there NaN values in the dataset?

Which columns tend to have NaN values?

How many NaN values are there per column?

Why do these columns have NaN values?

Challenge 3
Convert the birth_date column to Pandas Datetime objects

Add a Column called share_pct which has the laureates' share as a percentage in the form of a floating-point number."""

# Challenge 1
print(df_data.shape)
print(df_data.columns)
print(df_data.describe())
print(pd.to_numeric(df_data.year).min())
print(pd.to_numeric(df_data.year).max())
print(df_data.head())

# Challenge 2
print(df_data.duplicated().values.any())
print(df_data.isna().values.any())
print(df_data.isna().sum())
col_subset = ['year', 'category', 'laureate_type',
              'birth_date', 'full_name', 'organization_name']
print(df_data.loc[df_data.birth_date.isna()][col_subset])

# Challenge 3
df_data['birth_date'] = pd.to_datetime(df_data['birth_date'])

separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator
print(df_data.share_pct.head())
print(df_data.info())

"""Challenge 1: Come up with 3 Questions A big part of data science is coming up with questions that you'd like to 
explore. This is the most difficult aspect to teach in a tutorial because it's completely open-ended and requires 
some creativity. Often times you will be asking questions of the data, that it actually cannot answer - and that's 
ok. That's all part of the process of discovery. Pause here for a moment and think about the kind of data you saw in 
the columns. Write down at least 3 questions that you'd like to explore as part of this analysis. For example, 
your question might go like: "What percentage of the Nobel laureates were women?" or "How many prizes were given out 
in each category". Practice coming up with a few of your own questions. In the upcoming lessons, you might find that 
we will write the code to answer some of your questions. And if not, your questions make for a great exercise to take 
this analysis even further.

The challenges below are all based on questions we're going to ask the data:

Challenge 2 Create a donut chart using plotly which shows how many prizes went to men compared to how many prizes 
went to women. What percentage of all the prizes went to women?

Challenge 3
1.	What are the names of the first 3 female Nobel laureates?
2.	What did the win the prize for?
3.	What do you see in their birth_country? Were they part of an organization?

Challenge 4
Did some people get a Nobel Prize more than once? If so, who were they?

Challenge 5
1.	In how many categories are prizes awarded?
2.	Create a plotly bar chart with the number of prizes awarded by category.
3.	Use the color scale called Aggrnyl to color the chart, but don't show a color axis.
4.	Which category has the greatest number of prizes awarded?
5.	Which category has the fewest number of prizes awarded?

Challenge 6
1.	When was the first prize in the field of Economics awarded?
2.	Who did the prize go to?

Challenge 7
Create a plotly bar chart that shows the split between men and women by category.
Hover over the bar chart. How many prizes went to women in Literature compared to Physics?"""

# Challenge 1

# Will do soon !

# Challenge 2
percentage_gender = df_data.sex.value_counts()
print(percentage_gender.head())
male_vs_female_donut = px.pie(data_frame=percentage_gender, values=percentage_gender.values,
                              names=percentage_gender.index,
                              title='Male vs Female Noble Prize Winners', labels='index')
male_vs_female_donut.update_traces(textposition='outside', textinfo='percent+label', textfont_size=10, hole=0.4)
male_vs_female_donut.show()

# Challenge 3
print(df_data.loc[(df_data.sex == 'Female')].head(3))

# Challenge 4
print(df_data.loc[(df_data.full_name.duplicated())])

# Challenge 5
categories = df_data.category.value_counts()
category_bar_chart = px.bar(data_frame=categories, x=categories.index, y=categories.values,
                            title='Number of Prizes by Category',
                            labels=categories.index, color=categories.index,
                            color_discrete_sequence=px.colors.sequential.Aggrnyl)
category_bar_chart.show()

# Challenge 6
print(df_data.loc[(df_data.category == 'Economics')].head(1))
# categories = df_data.sex.value_counts()

# Challenge 7
cat_men_women = df_data.groupby(['category', 'sex'],
                                as_index=False).agg({'prize': pd.Series.count})
cat_men_women.sort_values('prize', ascending=False, inplace=True)
v_bar_split = px.bar(x=cat_men_women.category,
                     y=cat_men_women.prize,
                     color=cat_men_women.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')

v_bar_split.update_layout(xaxis_title='Nobel Prize Category',
                          yaxis_title='Number of Prizes')
v_bar_split.show()

"""Challenge 1
Are more prizes awarded recently than when the prize was first created? Show the trend in awards visually.
1.	Count the number of prizes awarded every year.
2.	Create a 5-year rolling average of the number of prizes (Hint: see previous lessons analyzing Google Trends).
3.	Using Matplotlib superimpose the rolling average on a scatter plot.
4.	Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).

5.	Use the named colors to draw the data points in dogerblue while the rolling average is colored in crimson.
6.	Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out?
7.	What could be the reason for the trend in the chart? 
 
 
Challenge 2
Investigate if more prizes are shared than before.
1.	Calculate the average prize share of the winners on a year by year basis.
2.	Calculate the 5-year rolling average of the percentage share.
3.	Copy-paste the cell from the chart you created above.
4.	Modify the code to add a secondary axis to your Matplotlib chart.
5.	Plot the rolling average of the prize share on this chart.
6.	See if you can invert the secondary y-axis to make the relationship even more clear."""

# Challenge 1
df_data['year'] = df_data['year'].astype(int)
prizes_per_year = df_data.groupby('year').agg({'prize': pd.Series.count})

prizes_per_year['rolling_avg'] = prizes_per_year.prize.rolling(5).mean()
# prizes_per_year.dropna(inplace=True)
print(prizes_per_year.head())

year_ticks = np.linspace(1900, 2020, (2020 - 1900) // 5, dtype=int)
print(year_ticks)

"""Draw the scatter plot via seaborn but without the line connecting the points."""
# with sns.axes_style('darkgrid'):
#     ax = sns.scatterplot(data=prizes_per_year, x='year', y='prize', color='blue',
#                          label='Prizes per Year', size='prize', hue='prize', style='rolling_avg')
#     ax.set(xlabel='Year', ylabel='Number of Prizes')
#     print(range(len(year_ticks)))
#     ax.set_xticks(year_ticks)
#     ax.set_xticklabels(year_ticks, rotation=45)

# plt.show()
"""Until here"""

prize_per_year = df_data.groupby(by='year').count().prize
moving_average = prizes_per_year.rolling(window=5).mean()
plt.figure(figsize=(8, 4), dpi=150)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax = plt.gca()  # get current axis
ax.set_xlim(1900, 2020)

ax.scatter(x=prize_per_year.index,
           y=prize_per_year.values,
           c='dodgerblue',
           alpha=0.7,
           s=100)

ax.plot(prize_per_year.index,
        moving_average.values,
        c='crimson',
        linewidth=3, )

# plt.show()

# Challenge 2
yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()

# plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()  # create second y-axis
ax1.set_xlim(1900, 2020)

# Can invert axis
ax2.invert_yaxis()

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100, )

ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3, )

# Adding prize share plot on second axis
ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',  # color of the line
         linewidth=3)  # thickness of the line

# plt.show()

"""Challenge 1: Top 20 Country Ranking
1.	Create a Pandas DataFrame called top20_countries that has the two columns. The prize column should contain 
the total number of prizes won.
2.	Is it best to use birth_country, birth_country_current or organization_country?
3.	What are some potential problems when using birth_country or any of the others? Which column is the least 
problematic?
4.	Then use plotly to create a horizontal bar chart showing the number of prizes won by each country. Here's what 
you're after:
5.	What is the ranking for the top 20 countries in terms of the number of prizes?
Challenge 2: 
1.	Choropleth Map
2.	Create this choropleth map using the plotly documentation:
3.	Experiment with plotly's available colors. I quite like the sequential color matter on this map.
Hint: You'll need to use a 3-letter country code for each country.
Challenge 3: Country Bar Chart with Prize Category
See if you can divide up the plotly bar chart you created above to show the which categories made up the 
total number of prizes. Here's what you're aiming for:
1.	In which category are Germany and Japan the weakest compared to the United States?
2.	In which category does Germany have more prizes than the UK?
3.	In which categories does France have more prizes than Germany?
4.	Which category makes up most of Australia's Nobel prizes?
5.	Which category makes up half of the prizes in the Netherlands?
6.	Does the United States have more prizes in Economics than all of France? What about in Physics or Medicine?
The hard part is preparing the data for this chart!
Hint: Take a two-step approach. The first step is grouping the data by country and category. Then you can create 
a DataFrame that looks something like this:
Challenge 4: Prizes by Country over Time
Every country's fortunes wax and wane over time. Investigate how the total number of prizes awarded changed 
over the years.
1.	When did the United States eclipse every other country in terms of the number of prizes won?
2.	Which country or countries were leading previously?
3.	Calculate the cumulative number of prizes won by each country in every year. Again, use the 
birth_country_current of the winner to calculate this.
Create a plotly line chart where each country is a colored line."""

# Challenge 1
top20_countries = df_data.groupby(by='birth_country_current').count().prize.sort_values(ascending=False).head(20)

top20_countries_bar_chart = px.bar(top20_countries,
                                   x=top20_countries.values,
                                   y=top20_countries.index,
                                   orientation='h',
                                   title='Top 20 Countries with the Most Nobel Prizes',
                                   color=top20_countries.values,
                                   color_continuous_scale='Viridis')
top20_countries_bar_chart.update_layout(xaxis_title='Number of Prizes',
                                        yaxis_title='Country',
                                        yaxis={'categoryorder': 'total ascending'})
top20_countries_bar_chart.show()

# Challenge 2
df_countries = df_data.groupby(['birth_country_current', 'ISO'],
                               as_index=False).agg({'prize': pd.Series.count})
print(df_countries.sort_values('prize', ascending=False))
# print(df_countries.ISO)

world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize',
                          hover_name='birth_country_current',
                          color_continuous_scale=px.colors.sequential.matter)
world_map.update_layout(coloraxis_showscale=True)
world_map.show()

# Challenge 3
df_countries_categories = df_data.groupby(['birth_country_current', 'category'],
                                          as_index=False).agg({'prize': pd.Series.count})
# print(df_countries_categories.head(10))

df_countries_categories.sort_values(by=['birth_country_current', 'prize'],
                                    ascending=[True, False], inplace=True)

merged_df = pd.merge(df_countries_categories, top20_countries, on='birth_country_current')
# change column names
merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize']
merged_df.sort_values(by='total_prize', inplace=True)

countries_categories_bar_chart = px.bar(x=merged_df.cat_prize,
                                        y=merged_df.birth_country_current,
                                        color=merged_df.category,
                                        orientation='h',
                                        title='Top 20 Countries by Number of Prizes and Category')

countries_categories_bar_chart.update_layout(xaxis_title='Number of Prizes',
                                             yaxis_title='Country')
countries_categories_bar_chart.show()

# Challenge 4
prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]

cumulative_prizes = prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum()
# print(cumulative_prizes)
cumulative_prizes.reset_index(inplace=True)  # reset index to get rid of multi-index
# print(cumulative_prizes)

l_chart = px.line(cumulative_prizes,
                  x='year',
                  y='prize',
                  color='birth_country_current',
                  hover_name='birth_country_current')

l_chart.update_layout(xaxis_title='Year',
                      yaxis_title='Number of Prizes')

l_chart.show()

"""Challenge 1
Many Nobel laureates are affiliated with a university, a laboratory, or a research organization (apart from Literature 
and Peace prize winners as we've seen). But the world is a big place. Which research institutions had the most 
Nobel laureates working there at the time of making the discovery?
Create a bar chart showing the organizations affiliated with the Nobel laureates. It should look something like this:
1.	Which organizations make up the top 20?
2.	How many Nobel prize winners are affiliated with the University of Chicago and Harvard University?
Challenge 2
Each research organization is located in a particular city. Are some cities hot spots for scientific discoveries? 
Where do major discoveries tend to take place?
1.	Create another plotly bar chart graphing the top 20 organization cities of the research institutions associated 
with a Nobel laureate.
2.	Where is the number one hotspot for discoveries in the world?
3.	Which city in Europe has had the most discoveries?
Challenge 3
Contrast the above chart with the birth city of the Nobel laureates. Would you expect to see a similar ranking for 
where the laureates are born versus where most discoveries are made? Would you expect to see the most populous cities 
producing the highest number of Nobel laureates? 
1.	Create a plotly bar chart graphing the top 20 birth cities of Nobel laureates.
2.	Use a named color scale called Plasma for the chart.
3.	What percentage of the United States prizes came from Nobel laureates born in New York?
4.	How many Nobel laureates were born in London, Paris and Vienna?
5.	Out of the top 5 cities, how many are in the United States?
Challenge 4
1.	Create a DataFrame that groups the number of prizes by organization.
2.	Then use the plotly documentation to create a sunburst chart
3.	Click around in your chart, what do you notice about Germany and France?"""

# Challenge 1
top20_orgs = df_data.groupby(by='organization_name').count().prize.sort_values(ascending=False).head(20)

top20_orgs_bar_chart = px.bar(top20_orgs,
                              x=top20_orgs.values,
                              y=top20_orgs.index,
                              orientation='h',
                              title='Top 20 Organizations with the Most Nobel Prizes',
                              color=top20_orgs.values,
                              color_continuous_scale='Viridis')
top20_orgs_bar_chart.update_layout(xaxis_title='Number of Prizes',
                                   yaxis_title='Organization',
                                   yaxis={'categoryorder': 'total ascending'})
top20_orgs_bar_chart.show()

# Challenge 2
df_orgs = df_data.groupby(['organization_name', 'organization_city'],
                          as_index=False).agg({'prize': pd.Series.count})
df_orgs.sort_values('prize', ascending=False, inplace=True, ignore_index=True)

top20_orgs_cities_bar_chart = px.bar(df_orgs.head(20),
                                     x='prize',
                                     y='organization_city',
                                     orientation='h',
                                     title='Top 20 Organization Cities with the Most Nobel Prizes',
                                     color='organization_name',
                                     color_continuous_scale=px.colors.sequential.Plasma)
top20_orgs_cities_bar_chart.update_layout(xaxis_title='Number of Prizes',
                                          yaxis_title='Organization',
                                          yaxis={'categoryorder': 'total ascending'})
top20_orgs_cities_bar_chart.show()

# Challenge 3
df_birth_cities = df_data.groupby(['birth_city', 'birth_country_current', 'organization_city'],
                                  as_index=False).agg({'prize': pd.Series.count})
df_birth_cities.sort_values('prize', ascending=False, inplace=True, ignore_index=True)

print(df_birth_cities.head(20))

top20_birth_cities_bar_chart = px.bar(df_birth_cities.head(20),
                                      x='prize',
                                      y='birth_city',
                                      orientation='h',
                                      title='Top 20 Birth Cities of Nobel Prize Winners',
                                      color='organization_city',
                                      color_continuous_scale=px.colors.sequential.Plasma)
top20_birth_cities_bar_chart.update_layout(xaxis_title='Number of Prizes',
                                           yaxis_title='Birth City',
                                           yaxis={'categoryorder': 'total ascending'})
top20_birth_cities_bar_chart.show()

# Challenge 4
country_city_org = df_data.groupby(by=['organization_country',
                                       'organization_city',
                                       'organization_name'], as_index=False).agg({'prize': pd.Series.count})

country_city_org = country_city_org.sort_values('prize', ascending=False)
burst = px.sunburst(country_city_org,
                    path=['organization_country', 'organization_city', 'organization_name'],
                    values='prize',
                    title='Where do Discoveries Take Place?',
                    )

burst.update_layout(xaxis_title='Number of Prizes',
                    yaxis_title='City',
                    coloraxis_showscale=True,
                    coloraxis_colorbar=dict(title='Number of Prizes'))

burst.show()

"""Challenge 1
Calculate the age of the laureate in the year of the ceremony and add this as a column called 
winning_age to the df_data DataFrame. Hint: you can use this to help you.

Challenge 2
Who were the oldest and the youngest winners?
1.	What are the names of the youngest and oldest Nobel laureate?
2.	What did they win the prize for?
3.	What is the average age of a winner?
4.	75% of laureates are younger than what age when they receive the prize?
5.	Use Seaborn to create histogram to visualize the distribution of laureate age at the time of winning. 
Experiment with the number of bins to see how the visualization changes.

Challenge 3
1.	Calculate the descriptive statistics for the age at the time of the award.
2.	Then visualize the distribution in the form of a histogram using Seaborn's .histplot() function.
3.	Experiment with the bin size. Try 10, 20, 30, and 50.

Challenge 4
Are Nobel laureates being nominated later in life than before? Have the ages of laureates at the time of the award 
increased or decreased over time?
1.	Use Seaborn to create a .regplot with a trendline.
2.	Set the lowess parameter to True to show a moving average of the linear fit.
3.	According to the best fit line, how old were Nobel laureates in the years 1900-1940 when they were awarded the prize?
4.	According to the best fit line, what age would it predict for a Nobel laureate in 2020?

Challenge 5
How does the age of laureates vary by category?
1.	Use Seaborn's .boxplot() to show how the mean, quartiles, max, and minimum values vary across categories. 
Which category has the longest "whiskers"?
2.	In which prize category are the average winners the oldest?
3.	In which prize category are the average winners the youngest?
4.	You can also use plotly to create the box plot if you like.

Challenge 6
1.	Now use Seaborn's .lmplot() and the row parameter to create 6 separate charts for each prize category. 
Again, set lowess to True.
2.	What are the winning age trends in each category?
3.	Which category has the age trending up and which category has the age trending down?
4.	Is this .lmplot() telling a different story from the .boxplot()?
5.	Create a third chart with Seaborn. This time use .lmplot() to put all 6 categories on the same chart 
using the hue parameter."""

# Challenge 1
df_data['winning_age'] = df_data['year'] - df_data['birth_date'].dt.year
# df_data.winning_age = df_data.winning_age.astype(int)
print(df_data.winning_age.head(20))
print(df_data.winning_age.describe())

# Challenge 2
print(df_data.nlargest(n=1, columns='winning_age'))
print(df_data.nsmallest(n=1, columns='winning_age'))

# Challenge 3
plt.figure(figsize=(8, 4), dpi=140)
sns.histplot(data=df_data,
             x=df_data.winning_age,
             bins=30)
plt.xlabel('Age')
plt.title('Distribution of Age on Receipt of Prize')
# plt.show()

plt.figure(figsize=(8, 4), dpi=140)
with sns.axes_style("whitegrid"):
    sns.regplot(data=df_data,
                x='year',
                y='winning_age',
                lowess=True,
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})

# plt.show()

plt.figure(figsize=(8, 4), dpi=140)
with sns.axes_style("whitegrid"):
    sns.boxplot(data=df_data,
                x='category',
                y='winning_age')

# plt.show()

with sns.axes_style("whitegrid"):
    sns.lmplot(data=df_data,
               x='year',
               y='winning_age',
               hue='category',
               lowess=True,
               aspect=2,
               scatter_kws={'alpha': 0.5},
               line_kws={'linewidth': 5})

plt.show()
