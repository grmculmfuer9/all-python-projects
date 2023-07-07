# Right: a > x & b = y
# Left: a < x & b = y
# Up: a = x & b > y
# Down: a = x & b < y

# Guardians of the Galaxy
def check_right(x_c, y_c, a_c, b_c):
    if a_c > x_c and b_c == y_c:
        return True
    return False


def check_left(x_c, y_c, a_c, b_c):
    if a_c < x_c and b_c == y_c:
        return True
    return False


def check_up(x_c, y_c, a_c, b_c):
    if a_c == x_c and b_c > y_c:
        return True
    return False


def check_down(x_c, y_c, a_c, b_c):
    if a_c == x_c and b_c < y_c:
        return True
    return False


# Galaxy
all_meteors = []
for x in range(int(input())):
    all_meteors.append(list(map(int, input().split())))

# Check for each meteor if they are a guardian
count = 0
for meteor in all_meteors:
    right = False
    left = False
    up = False
    down = False
    x, y = meteor[0], meteor[1]
    for rest_of_meteor in all_meteors:
        a, b = rest_of_meteor[0], rest_of_meteor[1]
        if check_right(x, y, a, b):
            right = True
        elif check_left(x, y, a, b):
            left = True
        elif check_up(x, y, a, b):
            up = True
        elif check_down(x, y, a, b):
            down = True
    if right and left and up and down:
        count += 1

print(count)
