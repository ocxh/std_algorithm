import sys

t = int(input())
for _ in range(t):
    n = int(input())
    people = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    people.sort()
    count = 1

    min_num = people[0][1]
    for i in range(n):
        if min_num > people[i][1]:
            min_num = people[i][1]
            count += 1
    print(count)
