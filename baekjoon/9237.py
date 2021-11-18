n = int(input())
an = list(map(int, input().split()))
an.sort(reverse=True)
count = 1 + len(an)
for i in range(0, n):
    an[i] -= n - (1 + i)
result = max(an) + count
print(result)
