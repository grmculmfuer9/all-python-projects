# Pizza Order Delivery
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want: S, M, or L? ")
add_pepperoni = input("Do you want pepproni? ")
extra_cheese = input("Do you want extra cheese? ")

s_p = 15
m_p = 20
l_p = 25

p_s_p = 2
p_m_l_p = 3

e_c = 1

price = 0

if size.lower() == "s":price = s_p
elif size.lower() == "m":price = m_p
else:price = l_p

if add_pepperoni.lower() == "y":
    if size.lower() == "s":price += p_s_p
    else:price += p_m_l_p

if extra_cheese.lower() == "y":price += e_c

print(f"Your final bill is ${price}")
