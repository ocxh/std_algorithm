n = int(input())
numbers = list(map(int, input().split()))
result=0

for i in range(len(numbers)):
    count=0
    for j in range(1, numbers[i]+1):
        if numbers[i]%j==0:
            count+=1
    if count==2:
        result+=1

print(result)
