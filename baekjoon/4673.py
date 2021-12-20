def sn(n):
    res = n + sum(list(map(int, str(n))))
    return res


none_sn = []
for i in range(1, 10000 + 1):
    none_sn.append(sn(i))

for i in range(1, 10000 + 1):
    if none_sn.count(i) == 0:
        print(i)
