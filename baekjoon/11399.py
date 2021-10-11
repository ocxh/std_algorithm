n = int(input())
p = list(map(int, input().split()))
p.sort()
count = [0] * (n)


for i in range(n):
    if i == 0:
        count[0] += p[0]
        continue
    count[i] = count[i - 1] + p[i]

print(sum(count))
