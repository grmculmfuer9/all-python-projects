# Tip Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
total_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? "))
final_price = (total_bill * (1 + tip/100)) / total_people
final_price = round(final_price, 2)
print("Each person should pay: $" + str(final_price))
