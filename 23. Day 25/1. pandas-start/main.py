# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [i[1] for i in data]
#     temperatures = [int(i) for i in temperatures[1:]]
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# Print specified column
print()
print(data["temp"])

# Convert data into dictionary
print()
data_dict = data.to_dict()
print(data_dict)

# Convert specified column into list
print()
temp_list = data["temp"].to_list()
print(temp_list)

# Get mean temperature
print()
mean_temp_data = data["temp"].mean()
print(mean_temp_data)

# Get max temperature
print()
max_value = data["temp"].max()
print(max_value)

# Get specified in two different ways
print()
print(data["condition"])
print()
print(data.condition)

# Get data in row
print()
print(data[data.day == "Monday"])
print()
print(data[data.temp == max_value])

# Convert Monday's temperature from Celsius to Fahrenheit
print()
monday = data[data.day == "Monday"]
print((monday.temp * (9/5)) + 32)

# Making DataFame from dictionary
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

# Convert this dictionary in csv file and store it at the specified location
data.to_csv("new_data.csv")
