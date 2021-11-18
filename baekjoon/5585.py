n = int(input())
result = 0
coin = [500, 100, 50, 10, 5, 1]

n = 1000 - n

for i in coin:
    result += n // i
    n %= i

print(result)
