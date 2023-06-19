import pandas as pd

df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")

print(len(df_pct_poverty))
print(len(df_pct_completed_hs))

merge_poverty_hs = pd.merge(df_pct_poverty,
                            df_pct_completed_hs,
                            on=['Geographic Area', 'City'])
print(df_pct_poverty.nunique())
print(df_pct_completed_hs.nunique())
print(merge_poverty_hs.nunique())
merge_poverty_hs.to_csv('merge_poverty_hs.csv', index=False)
print(len(merge_poverty_hs))
