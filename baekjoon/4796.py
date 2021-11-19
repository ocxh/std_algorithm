case = list()
while True:
    result = 0
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break

    result = min((a[2] % a[1]), a[0]) + a[0] * (a[2] // a[1])
    case.append(result)

for i in range(len(case)):
    print(f"Case {i+1}: {case[i]}")
