# Prime Number Checker

import math

#Write your code below this line 👇
def prime_checker(num):
    limit = math.sqrt(num)
    if num == 2 or num == 3:
        print("It's a prime number.")
    else:
        for i in range(1, int(limit)):
            if num % (i+1) == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(num=n)
