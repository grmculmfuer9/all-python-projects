import pandas
import os
import sys

# Get the absolute path to the directory containing the executable file
# base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

# Read CSV files
shopify_stock = pandas.read_csv(f"{base_path}/shopify_stock.csv")
stock_list = pandas.read_csv(f"{base_path}/stock_list.csv")

# Divide shopify stock in default title
default_title_shopify_stock = shopify_stock[shopify_stock["Option1 Value"] == "Default Title"]
non_default_title_shopify_stock = shopify_stock[shopify_stock["Option1 Value"] != "Default Title"]

# Initialize Updated Quantity and Updated Cost in shopify stock
default_title_shopify_stock["Updated Quantity"] = 0
default_title_shopify_stock["Updated Cost"] = 0

# Processing Default Title
title_shopify_stock = default_title_shopify_stock["Title"].tolist()
for x in title_shopify_stock:
    if x in stock_list["Item"].tolist():
        default_title_shopify_stock.loc[default_title_shopify_stock["Title"] == x, 'Updated Quantity'] = \
            stock_list.loc[stock_list["Item"] == x, 'Quantity'].values[0]
        default_title_shopify_stock.loc[default_title_shopify_stock["Title"] == x, 'Updated Cost'] = \
            stock_list.loc[stock_list["Item"] == x, 'Average Cost'].values[0]

# Processing Non Default Title
title_shopify_stock = non_default_title_shopify_stock["Option1 Value"].tolist()
for x in title_shopify_stock:
    if x in stock_list["Item"].tolist():
        non_default_title_shopify_stock.loc[non_default_title_shopify_stock["Option1 Value"] == x, 'Updated Quantity'] \
            = stock_list.loc[stock_list["Item"] == x, 'Quantity'].values[0]
        non_default_title_shopify_stock.loc[non_default_title_shopify_stock["Option1 Value"] == x, 'Updated Cost'] = \
            stock_list.loc[stock_list["Item"] == x, 'Average Cost'].values[0]

# Concatenate default and non default title
shopify_stock = pandas.concat([default_title_shopify_stock, non_default_title_shopify_stock])

# Export to CSV
shopify_stock.to_csv("shopify_stock_updated.csv", index=False)
