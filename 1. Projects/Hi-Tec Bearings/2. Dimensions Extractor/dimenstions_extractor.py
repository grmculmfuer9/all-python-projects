import pandas
import os
import sys
import re


def remove_html_tags(text_to_be_cleaned):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text_to_be_cleaned)


# Get the absolute path to the directory containing the executable file
# base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

# Read CSV files
df = pandas.read_csv(os.path.join(base_path, 'description_seperator.csv'))

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
    text = remove_html_tags(temp)
    for value in values_to_check:
        if value in text:
            start_index = text.find(value) + len(value) + 1
            end_index = 0
            for i in range(start_index, len(text)):
                if not text[i].isdigit() and text[i] != '.':
                    end_index = i
                    break
            if end_index == 0:
                continue
            overall_dimensions += f'{value}: {text[start_index:end_index]}\n'
            df[value][x[0]] = text[start_index:end_index]
    print(overall_dimensions)
    print('----------------------------------------')

# Save the dataframe to a CSV file
df.to_csv(os.path.join(base_path, 'description_seperator_updated.csv'), index=False)
