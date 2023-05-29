import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import scipy.stats as stats
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis

register_matplotlib_converters()

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv('monthly_deaths.csv',
                         parse_dates=['date'])

"""Challenge 1: Preliminary Data Exploration
1.	What is the shape of df_yearly and df_monthly? How many rows and columns?
2.	What are the column names?
3.	Which years are included in the dataset?
4.	Are there any NaN values or duplicates?
5.	What were the average number of births that took place per month?
6.	What were the average number of deaths that took place per month?"""

# Challenge 1
print(df_yearly.shape)
print(df_monthly.shape)

print(df_yearly.columns)
print(df_monthly.columns)

print(df_yearly['year'].unique())
print(df_monthly['date'].dt.year.unique())

print(df_yearly.isna().sum())
print(df_monthly.isna().sum())

print(df_yearly.duplicated().sum())
print(df_monthly.duplicated().sum())

print(df_monthly['births'].mean())
print(df_monthly['deaths'].mean())

"""Challenge 2: Percentage of Women Dying in Childbirth
How dangerous was childbirth in the 1840s in Vienna?
1.	Using the annual data, calculate the percentage of women giving birth who died throughout the 1840s at the hospital.
In comparison, the United States recorded 18.5 maternal deaths per 100,000 or 0.018% in 2013 (source)."""

# Challenge 2
prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')

print(type(df_monthly['date'][0]))

"""Challenge 3: Visualise the Total Number of Births 🤱 and Deaths 💀 over Time
Create a Matplotlib chart with twin y-axes. It should look something like this:
1.	Format the x-axis using locators for the years and months (Hint: we did this in the Google Trends notebook)
2.	Set the range on the x-axis so that the chart lines touch the y-axes
3.	Add gridlines
4.	Use skyblue and crimson for the line colours
5.	Use a dashed line style for the number of deaths
6.	Change the line thickness to 3 and 2 for the births and deaths respectively.
7.	Do you notice anything in the late 1840s?"""

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(9, 7), dpi=140)
plt.title('Total Number of Monthly Births and Deaths', fontsize=12)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Births', color='skyblue', fontsize=12)
ax2.set_ylabel('Deaths', color='crimson', fontsize=12)

# Use Locators
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color='grey', linestyle='--')

ax1.plot(df_monthly.date,
         df_monthly.births,
         color='skyblue',
         linewidth=3)

ax2.plot(df_monthly.date,
         df_monthly.deaths,
         color='crimson',
         linewidth=2,
         linestyle='--')

# plt.show()

"""Challenge 1: The Yearly Data Split by Clinic
Let's turn our attention to the annual data. Use plotly to create line charts of the births and deaths of the two 
different clinics at the Vienna General Hospital.
1.	Which clinic is bigger or more busy judging by the number of births?
2.	Has the hospital had more patients over time?
3.	What was the highest number of deaths recorded in clinic 1 and clinic 2?"""

# Challenge 1
line = px.line(df_yearly,
               x='year',
               y='births',
               color='clinic',
               title='Total Yearly Births by Clinic')

line.show()

line2 = px.line(df_yearly,
                x='year',
                y='deaths',
                color='clinic',
                title='Total Yearly Deaths by Clinic')

line2.show()

"""Challenge 2: Calculate the Proportion of Deaths at Each Clinic
Calculate the proportion of maternal deaths per clinic. That way we can compare like with like.
1.	Work out the percentage of deaths for each row in the df_yearly DataFrame by adding a column called "pct_deaths".
2.	Calculate the average maternal death rate for clinic 1 and clinic 2 (i.e., the total number of deaths per the 
total number of births).
3.	Create another plotly line chart to see how the percentage varies year over year with the two different clinics.
4.	Which clinic has a higher proportion of deaths?
5.	What is the highest monthly death rate in clinic 1 compared to clinic 2?"""

# Challenge 2
df_yearly['pct_deaths'] = df_yearly['deaths'] / df_yearly['births'] * 100

clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')

clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')

line3 = px.line(df_yearly,
                x='year',
                y='pct_deaths',
                color='clinic',
                title='Proportion of Yearly Deaths by Clinic')

line3.show()

"""Challenge 1: The Effect of Handwashing
1.	Add a column called "pct_deaths" to df_monthly that has the percentage of deaths per birth for each row.
2.	Create two subsets from the df_monthly data: before and after Dr Semmelweis ordered washing hand.
3.	Calculate the average death rate prior to June 1846.
4.	Calculate the average death rate after June 1846.

Challenge 2: Calculate a Rolling Average of the Death Rate
Create a DataFrame that has the 6-month rolling average death rate prior to mandatory handwashing.
Hint: You'll need to set the dates as the index in order to avoid the date column being dropped during the calculation

Challenge 3: Highlighting Subsections of a Line Chart
Copy-paste and then modify the Matplotlib chart from before to plot the monthly death rates 
(instead of the total number of births and deaths). The chart should look something like this:
1.	Add 3 separate lines to the plot: the death rate before handwashing, after handwashing, 
and the 6-month moving average before handwashing.
2.	Show the monthly death rate before handwashing as a thin dashed black line.
3.	Show the moving average as a thicker, crimson line.
4.	Show the rate after handwashing as a skyblue line with round markers.
5.	Look at the code snippet in the documentation to see how you can add a legend to the chart."""

# Challenge 1
df_monthly['pct_deaths'] = df_monthly['deaths'] / df_monthly['births'] * 100
scrape_date = pd.to_datetime('1846-06-01')
before = df_monthly[df_monthly.date < scrape_date]
after = df_monthly[df_monthly.date >= scrape_date]

# Challenge 2
print('Challenge 2')
rolling_avg = before.set_index('date').rolling(window=6).mean()
print(before.set_index('date'))
print(rolling_avg)
df_monthly['rolling_avg'] = rolling_avg['pct_deaths']

# Challenge 3
plt.figure(figsize=(9, 7), dpi=140)
plt.title('Percentage of Monthly Deaths over Time', fontsize=12)
plt.yticks(fontsize=8)
plt.xticks(fontsize=8, rotation=45)

plt.ylabel('Percentage of Deaths', color='crimson', fontsize=12)

ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.grid(color='grey', linestyle='--')

ma_line, = plt.plot(rolling_avg.index,
                    rolling_avg.pct_deaths,
                    color='crimson',
                    linewidth=3,
                    linestyle='--',
                    label='6m Moving Average')
bw_line, = plt.plot(before.date,
                    before.pct_deaths,
                    color='black',
                    linewidth=1,
                    linestyle='--',
                    label='Before Handwashing')
aw_line, = plt.plot(after.date,
                    after.pct_deaths,
                    color='skyblue',
                    linewidth=3,
                    marker='o',
                    label='After Handwashing')

plt.legend(handles=[ma_line, bw_line, aw_line],
           fontsize=18)

# plt.show()

"""Challenge 1: Calculate the Difference in the Average Monthly Death Rate
1.	What was the average percentage of monthly deaths before handwashing (i.e., before June 1847)?
2.	What was the average percentage of monthly deaths after handwashing was made obligatory?
3.	By how much did handwashing reduce the average chance of dying in childbirth in percentage terms?
4.	How do these numbers compare to the average for all the 1840s that we calculated earlier?
5.	How many times lower are the chances of dying after handwashing compared to before?"""

# Challenge 1
avg_prob_before = before.pct_deaths.mean()
print(f'Chance of death during childbirth before handwashing: {avg_prob_before:.3}%.')

avg_prob_after = after.pct_deaths.mean()
print(f'Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.')

mean_diff = avg_prob_before - avg_prob_after
print(f'Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!')

times = avg_prob_before / avg_prob_after
print(f'This is a {times:.2}x improvement!')

"""Challenge 2: Using Box Plots to Show How the Death Rate Changed Before and After Handwashing
The statistic above is impressive, but how do we show it graphically? With a box plot we can show how the quartiles, 
minimum, and maximum values changed in addition to the mean.
1.	Use NumPy's .where() function to add a column to df_monthly that shows if a particular date was before or 
after the start of handwashing.
2.	Then use plotly to create box plot of the data before and after handwashing.
3.	How did key statistics like the mean, max, min, 1st and 3rd quartile changed as a result of the new policy"""

# Challenge 2
print(df_monthly)
df_monthly['handwashing_started'] = np.where(df_monthly.date < scrape_date, 'before', 'after')

box = px.box(df_monthly,
             x='handwashing_started',
             y='pct_deaths',
             color='handwashing_started',
             title='How Have the Stats Changed with Handwashing?')

box.update_layout(xaxis_title='Washing Hands?',
                  yaxis_title='Percentage of Monthly Deaths', )

box.show()

"""Challenge 3: Use Histograms to Visualise the Monthly Distribution of Outcomes
Create a plotly histogram to show the monthly percentage of deaths.
1.	Use docs to check out the available parameters. Use the color parameter to display two overlapping histograms.
2.	The time period of handwashing is shorter than not handwashing. Change histnorm to percent 
to make the time periods comparable.
3.	Make the histograms slightly transparent
4.	Experiment with the number of bins on the histogram. Which number works well in communicating the range of outcomes?
5.	Just for fun, display your box plot on the top of the histogram using the marginal parameter"""

hist = px.histogram(df_monthly,
                    x='pct_deaths',
                    color='handwashing_started',
                    nbins=30,
                    opacity=0.6,
                    barmode='overlay',
                    histnorm='percent',
                    marginal='box')

hist.update_layout(xaxis_title='Proportion of Monthly Deaths',
                   yaxis_title='Count', )

hist.show()

"""Challenge 4: Use a Kernel Density Estimate (KDE) to visualise a smooth distribution
Use Seaborn's .kdeplot() to create two kernel density estimates of the pct_deaths, one for before handwashing 
and one for after.
1.	Use the shade parameter to give your two distributions different colours.
2.	What weakness in the chart do you see when you just use the default parameters?
3.	Use the clip parameter to address the problem."""

print(before.pct_deaths)
print(after.pct_deaths)

before['pct_deaths'] /= 100
after['pct_deaths'] /= 100

plt.figure(figsize=(9, 7), dpi=140)
sns.kdeplot(before.pct_deaths,
            fill=True,
            clip=(0, 1))
sns.kdeplot(after.pct_deaths,
            fill=True,
            clip=(0, 1))
plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.xlim(0, 0.40)
plt.show()

"""Challenge 5: Use a T-Test to Show Statistical Significance
Use a t-test to determine if the differences in the means are statistically significant or purely due to chance.
If the p-value is less than 1% then we can be 99% certain that handwashing has made a difference to the 
average monthly death rate.
1.	Import stats from scipy
2.	Use the .ttest_ind() function to calculate the t-statistic and the p-value
3.	Is the difference in the average proportion of monthly deaths statistically significant at the 99% level?"""

t_stat, p_value = stats.ttest_ind(a=before.pct_deaths,
                                  b=after.pct_deaths)
print(f'p-value is {p_value:.10f}')
print(f't-statistic is {t_stat:.4}')
