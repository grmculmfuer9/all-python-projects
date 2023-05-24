import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
pd.options.display.float_format = '{:,.2f}'.format # to display all the numbers with 2 decimal places
columns = df.columns
print('columns: ', columns)

"""What college major has the highest mid-career salary? 
How much do graduates with this major earn? 
(Mid-career is defined as having 10+ years of experience)"""
highest_mid_career_salary = df.loc[df['Mid-Career Median Salary'].idxmax()]
print(f"Major with the highest mid-career salary is {highest_mid_career_salary['Undergraduate Major']}"
      f"and gets paid {highest_mid_career_salary['Mid-Career Median Salary']}")

"""Which college major has the lowest starting salary and how much do graduates earn after university?"""
lowest_starting_salary = df.loc[df['Starting Median Salary'].idxmin()]
print(f"Major with the lowest starting salary is {lowest_starting_salary['Undergraduate Major']}"
      f"and gets paid {lowest_starting_salary['Starting Median Salary']} after university")

"""Which college major has the lowest mid-career salary and 
how much can people expect to earn with this degree?"""
lowest_mid_career_salary = df.loc[df['Mid-Career Median Salary'].idxmin()]
print(f"Major with the lowest mid-career salary is {lowest_mid_career_salary['Undergraduate Major']}"
      f"and gets paid {lowest_mid_career_salary['Mid-Career Median Salary']}")

# Insert a new column into the DataFrame that shows the difference between starting and mid-career salary.
spread_col = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']
df.insert(1, 'Spread', spread_col)
print(df.head())

"""Using the .sort_values() method, can you find the degrees with the highest potential?
Find the top 5 degrees with the highest values in the 90th percentile."""
highest_potential = df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potential.head())

"""Using the .sort_values() method, can you find the degrees with the greatest spread in salaries?"""
greatest_spread = df.sort_values(by='Spread', ascending=False)
print(greatest_spread.head())

print(df.groupby('Group').count())
print(df.groupby('Group').mean())
