import pandas as pd

from pandas.plotting import register_matplotlib_converters

# import numpy as np
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis

register_matplotlib_converters()

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv('monthly_deaths.csv',
                         parse_dates=['date'])
