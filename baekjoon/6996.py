n = int(input())
li = []
for i in range(n):
    li.append(list(input().split()))

for i in range(n):
    if len(li[i][0]) != len(li[i][1]):
        print(li[i][0], "&", li[i][1], "are NOT anagrams.")
        continue

    count = 0
    buffer = li[i][1]
    for j in range(len(li[i][0])):
        if li[i][0][j] in buffer:
            count += 1
            buffer = buffer.replace(li[i][0][j], "", 1)
    if count == len(li[i][0]):
        print(li[i][0], "&", li[i][1], "are anagrams.")
    else:
        print(li[i][0], "&", li[i][1], "are NOT anagrams.")
