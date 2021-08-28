#구현 예제 4-1 상하좌우
n = int(input()) - 1
mov = list(input().split())

x=0
y=0

for i in mov:
    if i == 'L' and y != 0:
        y -= 1
    elif i == 'R' and y != n:
        y += 1
    elif i == 'U' and x != 0:
        x -= 1
    elif i == 'D' and x != n:
        x += 1

x+=1
y+=1


print(x, y)


