import matplotlib.pyplot as plt
import pandas as pd

colors = pd.read_csv('data/colors.csv')
sets = pd.read_csv('data/sets.csv')
themes = pd.read_csv('data/themes.csv')

# Colors
print(colors['name'].nunique())
print(colors.tail())

# Sets
year_id_min = sets['year'].idxmin()
print()
print(f'{sets["name"].loc[year_id_min]} was the first set released in {sets["year"].loc[year_id_min]}')
# How many products did the LEGO company sell in their first year of operation?
print(
    f'These many {sets.loc[sets["year"] == sets["year"].loc[year_id_min]].name.count()} products were sold in the '
    f'first year')
top_five_sets = sets.sort_values(by="num_parts", ascending=False).head().name.to_list()
top_five_sets = list(set(top_five_sets))
print(f'The top five sets are: {top_five_sets}')

sets_by_year = sets.groupby('year').count()
print(sets_by_year.head())
print(sets_by_year.tail())

themes_by_year = sets.groupby('year').agg(func={'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
print(themes_by_year.head())

parts_per_set = sets.groupby('year').agg(func={'num_parts': pd.Series.mean})
print(parts_per_set.head())
print(parts_per_set.tail())

set_theme_count = sets.theme_id.value_counts()
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
print(set_theme_count.head())

merged_df = pd.merge(themes, set_theme_count, on='id')
print()
print(merged_df.head())

plt.figure(figsize=(10, 10))
plt.xlim(1950, 2018)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index, sets_by_year['num_parts'], linewidth=3, color='green', label='Number of Parts')
ax2.plot(themes_by_year.index, themes_by_year['nr_themes'], linewidth=3, color='blue', label='Number of Themes')

ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Number of Parts', fontsize=10, color='green')
ax2.set_ylabel('Number of Themes', fontsize=10, color='blue')

ax1.legend(fontsize=10)
ax2.legend(fontsize=10)

plt.scatter(parts_per_set.index, parts_per_set.num_parts, label='Parts per Set', color='red', s=100)

plt.figure(figsize=(12, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.show()
