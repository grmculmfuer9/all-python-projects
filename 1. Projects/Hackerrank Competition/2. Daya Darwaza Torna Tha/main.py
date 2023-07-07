# Daya Darwaza Torna Tha
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = a

count = 0
ans = 0
if y >= x:
    for i in range(n):
        if b[i] > x:
            break
        ans += 1
else:
    ans = n
print(ans)
