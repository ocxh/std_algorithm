#구현 예제 4-2 시각 

n = int(input())
count = 0

for x in range(n+1):
    for y in range(60):
        for z in range(60):
            if '3' in str(x)+str(y)+str(z):
                count += 1

print(count)