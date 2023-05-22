# Words Calculator

print("Welcoome to the words calculator")
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

name_1 = name_1.lower()
name_2 = name_2.lower()
combined_string = name_1 + name_2

total = 0
# t = r = u = l = v = o = e = total = 0

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")

true = t + r + u + e
love = l + o + v + e
total = str(true) + str(love)
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are all right together.")
else:
    print(f"Your score is {total}")

print(f"t is {t}, r is {r}, u is {u}, l is {l}, v is {v}, o is {o}, e is {e}")
