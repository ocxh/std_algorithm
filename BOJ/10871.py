n, x = map(int, input().split())
arr = list(map(int, input().split()))
darr = []
for i in range(n):
    if x > arr[i]:
        darr.append(arr[i])

for i in range(len(darr)):
    print(darr[i], end=" ")
