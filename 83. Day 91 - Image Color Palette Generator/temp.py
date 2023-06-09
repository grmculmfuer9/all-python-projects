import pandas
import re

from tkinter.filedialog import askopenfilename
from tkinter import filedialog


def upload_csv_file(filename):
    filepath = ''
    while filepath == '':
        filepath = askopenfilename(filetypes=[(filename, '*.csv')])
    return filepath


print('Which program do you want to run?')
print('1. Update Quantity and Cost')
print('2. Extract Data from HTML Tags')

choice = ''

while choice != '1' and choice != '2':
    choice = input('Enter your choice: ')
print(choice)

if choice == '1':
    print('entered 1')
    stock_list_path = ''
    shopify_stock_path = ''

    upload_csv_file('Stock List CSV')
    # while stock_list_path == '':
    #     print('entered while')
    #     stock_list_path = filedialog.askopenfilename(filetypes=[('Stock List CSV', '*.csv')])

    while shopify_stock_path == '':
        print('entered while')
        shopify_stock_path = askopenfilename(filetypes=[('Shopify Stock CSV', '*.csv')])

    # # Get the absolute path to the directory containing the executable file
    # # base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

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
else:
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


    # # Get the absolute path to the directory containing the executable file
    # # base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

    shopify_stock_path = ''

    while shopify_stock_path == '':
        shopify_stock_path = askopenfilename(filetypes=[('Shopify Stock CSV', '*.csv')])

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
