import re
import tkinter as tk
from tkinter.filedialog import askopenfilename

import pandas


def remove_html_tags(text_to_be_cleaned):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text_to_be_cleaned)


def check_int_float(string):
    """Check if a string is an integer or a float"""
    try:
        float(string)
        return True
    except ValueError:
        return False


def open_file(filename):
    filepath = ''
    while filepath == '':
        error.config(text=f'Please select a {filename} file', fg='red')
        filepath = askopenfilename(filetypes=[(filename, '*.csv')])
    return filepath


def update_quantity_and_pricing():
    stock_list_path = open_file('Stock List CSV')
    shopify_stock_path = open_file('Shopify Stock CSV')

    # Read CSV files
    shopify_stock = pandas.read_csv(shopify_stock_path)
    stock_list = pandas.read_csv(stock_list_path)

    # Divide shopify stock in default title
    default_title_shopify_stock = shopify_stock[shopify_stock["Option1 Value"] == "Default Title"]
    non_default_title_shopify_stock = shopify_stock[shopify_stock["Option1 Value"] != "Default Title"]

    # Initialize Updated Quantity and Updated Cost in shopify stock
    default_title_shopify_stock["Updated Quantity"] = 0
    default_title_shopify_stock["Updated Cost"] = 0

    # Processing Default Title
    title_shopify_stock = default_title_shopify_stock["Title"].tolist()
    for x in title_shopify_stock:
        if x in stock_list[stock_list['Brand'] == 'HI-TEC']["Item"].tolist():
            print('original', x)
            print(stock_list.loc[
                      (stock_list["Item"] == x) & (stock_list['Brand'] == 'HI-TEC'), ['Quantity',
                                                                                      'Average Cost']].values[
                      0])
            print('change')
            print(stock_list.loc[(stock_list["Item"] == x) & (stock_list['Brand'] == 'HI-TEC'), 'Quantity'].values)
            default_title_shopify_stock.loc[
                default_title_shopify_stock["Title"] == x, ['Updated Quantity', 'Updated Cost']] = stock_list.loc[
                (stock_list["Item"] == x) & (stock_list['Brand'] == 'HI-TEC'), ['Quantity', 'Average Cost']].values[0]

    # Processing Non Default Title
    title_shopify_stock = non_default_title_shopify_stock["Option1 Value"].tolist()
    for x in title_shopify_stock:
        if x in stock_list[stock_list['Brand'] == 'HI-TEC']["Item"].tolist():
            non_default_title_shopify_stock.loc[
                non_default_title_shopify_stock["Option1 Value"] == x, ['Updated Quantity', 'Updated Cost']] = \
                stock_list.loc[
                    (stock_list["Item"] == x) & (stock_list['Brand'] == 'HI-TEC'), ['Quantity', 'Average Cost']].values[
                    0]

    # Concatenate default and non default title
    shopify_stock = pandas.concat([default_title_shopify_stock, non_default_title_shopify_stock])

    # Get the path of the shopify stock
    updated_file_path = shopify_stock_path.split('/')
    updated_file_path[-1] = 'updated_' + updated_file_path[-1]
    updated_file_path = '/'.join(updated_file_path)

    # Export to CSV
    shopify_stock.to_csv(updated_file_path, index=False)

    error.config(text='Quantity and Pricing has been updated!', fg='green')


def extract_data_from_html():
    # # Get the absolute path to the directory containing the executable file
    # # base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

    shopify_stock_path = open_file('Shopify Stock CSV')

    # Read CSV files
    df = pandas.read_csv(shopify_stock_path)

    # Drop rows with empty values in column 'Body (HTML)'
    df = df.dropna(subset=['Body (HTML)'])

    # Initialize bore diameter, outside diameter and width
    df['bore diameter'] = ""
    df['outside diameter'] = ""
    df['width'] = ""

    values_to_check = ['outside diameter', 'bore diameter', 'width']
    for x in df.iterrows():
        overall_dimensions = ""
        temp = str(x[1]['Body (HTML)']).lower()
        text = [x for x in remove_html_tags(temp).split('\n') if x != '']
        for value in values_to_check:
            if value in text:
                index = text.index(value) + 1
                if check_int_float(text[index]):
                    overall_dimensions += f'{value}: {text[index]}\n'
                    df[value][x[0]] = text[index]
            elif value == 'width':
                print('check width', 'total width' in text)
                if 'total width' in text:
                    index = text.index('total width') + 1
                    if check_int_float(text[index]):
                        overall_dimensions += f'{value}: {text[index]}\n'
                        df[value][x[0]] = text[index]
            else:
                for temp in text:
                    if value in temp:
                        index = text.index(temp) + 1
                        if check_int_float(text[index]):
                            overall_dimensions += f'{value}: {text[index]}\n'
                            df[value][x[0]] = text[index]
        print(overall_dimensions)
        print('----------------------------------------')

    # Get the path of the shopify stock
    updated_file_path = shopify_stock_path.split('/')
    updated_file_path[-1] = 'updated_' + updated_file_path[-1]
    updated_file_path = '/'.join(updated_file_path)

    # Save the dataframe to a CSV file
    df.to_csv(updated_file_path, index=False)

    error.config(text='Dimensions has been successfully updated!', fg='green')


def variants_detection():
    shopify_stock_path = open_file('Shopify Stock CSV')

    # Read CSV file
    df = pandas.read_csv(shopify_stock_path)

    # Add columns Bore, Cage, and Seal Type
    df['Bore'] = ""
    df['Cage'] = ""
    df['Seal Type'] = ""

    # Divide df into 2 dataframes (default title and non default title)
    # default_title_shopify_stock = df[df['Option1 Value'] == 'Default Title']
    non_default_title_shopify_stock = df[df['Option1 Value'] != 'Default Title']['Option1 Value'].tolist()

    # Initialize bore diameter, outside diameter and width
    bore_possible_variants = ['k']
    bore_possible_variants_name = ['Tapered']

    cage_possible_variants = ['e', 'f', 'm', 'ecp', 'ca', 'mb', 'cc']
    cage_possible_variants_name = ['Steel', 'Fibre', 'Brass', 'Polyamide', 'Brass', 'Steel', 'Brass']

    sealtype_possible_variants = ['2rs', 'rs', 'z', '2z']
    sealtype_possible_variants_name = ['2RS', 'rs', 'z', '2z']

    # for item in non_default_title_shopify_stock['Option1 Value'].tolist():
    for item in non_default_title_shopify_stock:
        # Check Bore
        item_individual = item.lower().split()

        if check_int_float(item_individual[-1]):
            df.loc[df['Option1 Value'] == item, 'Bore'] = 'Plain'
            df.loc[df['Option1 Value'] == item, 'Cage'] = 'Steel'
        else:
            for value in item_individual:
                print(df.loc[df['Option1 Value'] == item, 'Bore'])
                # print(df.loc[df['Option1 Value'] == item, 'Bore'][0])
                # print(df.loc[df['Option1 Value'] == item, 'Bore'][1])
                # print('value')
                if value in bore_possible_variants:
                    print(value, value in bore_possible_variants, 'bore')
                    index = bore_possible_variants.index(value)
                    df.loc[df['Option1 Value'] == item, 'Bore'] = bore_possible_variants_name[index]

                if value in cage_possible_variants:
                    print(value, value in cage_possible_variants, 'cage')
                    index = cage_possible_variants.index(value)
                    df.loc[df['Option1 Value'] == item, 'Cage'] = cage_possible_variants_name[index]

                if value in sealtype_possible_variants:
                    print(value, value in sealtype_possible_variants, 'sealtype')
                    index = sealtype_possible_variants.index(value)
                    df.loc[df['Option1 Value'] == item, 'Seal Type'] = sealtype_possible_variants_name[
                        index]

        # Get the path of the shopify stock
        updated_file_path = shopify_stock_path.split('/')
        updated_file_path[-1] = 'updated_' + updated_file_path[-1]
        updated_file_path = '/'.join(updated_file_path)

        df.to_csv(updated_file_path, index=False)

        error.config(text='Variants has been successfully updated!', fg='green')


root = tk.Tk()
root.config(bg='#E6FFFD')
root.title('Shopify Stock Updater')
root.geometry('900x800')
root.resizable(False, False)

# Title
title = tk.Label(root, text="Shopify Stock Updater", font=("Arial", 30), bg="#E6FFFD", fg="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

# Label
label = tk.Label(root, text="Choose an option:", font=("Arial", 20), bg="#E6FFFD", fg="#B799FF")
label.place(relx=0.5, rely=0.3, anchor="center")

# Update Quantity and Pricing Button
update_quantity_pricing = tk.Button(root, text="Update Quantity and Pricing", font=("Arial", 20), bg="#B799FF",
                                    fg="#E6FFFD", command=update_quantity_and_pricing)
update_quantity_pricing.place(relx=0.5, rely=0.4, anchor="center")

# Extract Data from HTML Button
extract_data_html = tk.Button(root, text="Extract Data from HTML", font=("Arial", 20), bg="#B799FF",
                              fg="#E6FFFD", command=extract_data_from_html)
extract_data_html.place(relx=0.5, rely=0.5, anchor="center")

# Variant Column Adding Button
variant_column_adding = tk.Button(root, text="Variant Column Adding", font=("Arial", 20), bg="#B799FF",
                                  fg="#E6FFFD", command=variants_detection)
variant_column_adding.place(relx=0.5, rely=0.6, anchor="center")

# Error
error = tk.Label(root, text="", font=("Arial", 20), bg="#E6FFFD", fg="red")
error.place(relx=0.5, rely=0.7, anchor="center")

# Mainloop
root.mainloop()
