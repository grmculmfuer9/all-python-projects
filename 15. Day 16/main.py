# PrettyTable to make the beautiful table
from prettytable import PrettyTable
x = PrettyTable()
x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Type", ["Electric", "Water", "Fire"])
x.align = "l"
print(x)
