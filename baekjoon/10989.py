import sys

n = int(sys.stdin.readline())
count = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if i == 0:
        continue
    for j in range(count[i]):
        print(i)
