import math

m = int(input())
n= int(input())

arr = [True for i in range(n+1)]
result = list()
arr[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j=2
        while i*j<=n:
            arr[i*j] = False
            j+=1

for i in range(m, n+1):
    if arr[i]:
        result.append(i)

if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
