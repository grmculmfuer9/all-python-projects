import pandas as pd
from pandas.plotting import register_matplotlib_converters

pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()
data = pd.read_csv('cost_revenue_dirty.csv')
