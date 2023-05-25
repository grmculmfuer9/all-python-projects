from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

lst = [df_tesla, df_btc_search, df_btc_price, df_unemployment]

for x in lst:
    if x.isna().values.any():
        print('True')
        print(x.isna().values.sum())
        print(x.isnull())
        x.dropna(inplace=True)

print('here')

for x in lst:
    if 'DATE' in x and not isinstance(x['DATE'][0], datetime):
        x['DATE'] = pd.to_datetime(x['DATE'])
        print(type(x['DATE'][0]))
    elif 'MONTH' in x and not isinstance(x['MONTH'][0], datetime):
        x['MONTH'] = pd.to_datetime(x['MONTH'])
        print(type(x['MONTH'][0]))

df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

print(df_btc_monthly.head())

# Matplotlib
register_matplotlib_converters()

# # Tesla Stock Price
# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Tesla Web Search vs Price', fontsize=18)
#
# ax1 = plt.gca()  # get current axis
# ax2 = ax1.twinx()
#
# ax1.set_xlabel('Year', fontsize=14)
# ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)  # can use a HEX code
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)  # or a named colour
#
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
#
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
#
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_minor_locator(months)
# ax1.xaxis.set_major_formatter(years_fmt)
#
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
#
# # BTC Price
# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
#
# ax1 = plt.gca()  # get current axis
# ax2 = ax1.twinx()
#
# ax1.set_xlabel('Year', fontsize=14)
# ax1.set_ylabel('BTC Price', color='#E6232E', fontsize=14)  # can use a HEX code
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)  # or a named colour
#
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
#
# ax1.set_ylim(bottom=0, top=15000)
# ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_minor_locator(months)
# ax1.xaxis.set_major_formatter(years_fmt)
#
# ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
#          color='#F08F2E', linewidth=3, linestyle='dashed')
# ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
#          color='skyblue', linewidth=3, marker='o')

# # Unemployment Benefits 2019
# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
#
# ax1 = plt.gca()  # get current axis
# ax2 = ax1.twinx()
#
# ax1.set_xlabel('Year', fontsize=14)
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)  # can use a HEX code
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)  # or a named colour
#
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
#
# ax1.set_ylim(bottom=df_unemployment.UNRATE.min(), top=df_unemployment.UNRATE.max())
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_minor_locator(months)
# ax1.xaxis.set_major_formatter(years_fmt)
#
# ax1.grid(color='grey', linestyle='--')
#
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
#
# ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
# ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

# Unemployment Benefits 2020
plt.figure(figsize=(14, 8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()
