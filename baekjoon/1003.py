one_li = [0, 1]
zero_li = [1, 0]

for i in range(2, 40 + 1):
    one_li.append(one_li[i - 1] + one_li[i - 2])
    zero_li.append(one_li[i - 1])

t = int(input())
for i in range(t):
    n = int(input())
    print(zero_li[n], one_li[n])
