import random

import pandas as pd
import plotly.express as px

pd.options.display.float_format = '{:,.2f}'.format
df_apps = pd.read_csv('apps.csv')

print(df_apps.shape)
print(df_apps.head())
print(df_apps.sample(5))

df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)

print(df_apps.isna().values.sum())
df_apps.dropna(inplace=True)
if df_apps.duplicated().values.any():
    df_apps.drop_duplicates(inplace=True, subset=['App', 'Type', 'Price'])

print(df_apps.sort_values(ascending=False, by='Rating').head(10))
print(df_apps.sort_values('Size_MBs', ascending=False).head())
top_fifty_apps = df_apps.sort_values('Reviews', ascending=False).head(50)
print(top_fifty_apps[top_fifty_apps['Price'] != '0'].count())

ratings = df_apps.Content_Rating.value_counts()

print(df_apps.info())
df_apps.Installs = df_apps.Installs.astype(str).str.replace(',', "")
df_apps.Installs = pd.to_numeric(df_apps.Installs)
print(df_apps[['App', 'Installs']].groupby('Installs').count())

print(df_apps.Price.describe())
df_apps.Price = df_apps.Price.astype(str).str.replace('$', "")
df_apps.Price = pd.to_numeric(df_apps.Price)

df_apps.sort_values('Price', ascending=False).head(20)

df_apps = df_apps[df_apps['Price'] < 250]
df_apps.sort_values('Price', ascending=False).head(5)

df_apps['Revenue_Estimate'] = df_apps.Installs.mul(df_apps.Price)
print(df_apps.sort_values(by='Revenue_Estimate', ascending=False).head(10))

print(df_apps.Category.nunique())
top10_category = df_apps.Category.value_counts()[:10]

category_installs = df_apps.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

cat_number = df_apps.groupby('Category').agg({'App': pd.Series.count})

cat_merged_df = pd.merge(cat_number, category_installs, on='Category')
print(cat_merged_df.columns)
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
print(cat_merged_df.sort_values('Installs', ascending=False))

# Split the strings on the semicolon and then .stack them.
stack = df_apps.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

df_free_vs_paid = df_apps.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
print(df_free_vs_paid.head())

df_paid_apps = df_apps[df_apps['Type'] == 'Paid']

print(df_paid_apps.Price.median())

# Plotly Express
fig = px.pie(labels=ratings.index, values=ratings.values, title='Content Rating', names=ratings.index)
fig.update_traces(textposition='outside', textinfo='percent+label', textfont_size=10, hole=0.6)

bar = px.bar(x=num_genres.index[:15],  # index = category name
             y=num_genres.values[:15],  # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale=random.choice(px.colors.named_colorscales()))

bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps')

h_bar = px.bar(x=category_installs.Installs,
               y=category_installs.index,
               orientation='h',
               title='Category Popularity')

scatter = px.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs")

h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               barmode='group',
               color='Type')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

box = px.box(df_apps,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='outliers',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))

box_app_earnings = px.box(df_paid_apps,
                          x='Category',
                          y='Revenue_Estimate',
                          title='How Much Can Paid Apps Earn?')

box_app_earnings.update_layout(xaxis_title='Category',
                               yaxis_title='Paid App Ballpark Revenue',
                               xaxis={'categoryorder': 'min ascending'},
                               yaxis=dict(type='log'))

box_app_pricing = px.box(df_paid_apps,
                         x='Category',
                         y="Price",
                         title='Price per Category')

box_app_pricing.update_layout(xaxis_title='Category',
                              yaxis_title='Paid App Price',
                              xaxis={'categoryorder': 'max descending'},
                              yaxis=dict(type='log'))

fig.show()
bar.show()
h_bar.show()
scatter.show()
g_bar.show()
box.show()
box_app_earnings.show()
box_app_pricing.show()
