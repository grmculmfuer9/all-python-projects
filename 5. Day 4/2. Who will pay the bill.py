# Who will pay the bill?
import random

names = input("Give me everybody's names, separted by comma \", \": ").split(", ")
x = len(names)
ran = random.randint(0, x-1)
print(f"{names[ran]} will pay the meal today.")
