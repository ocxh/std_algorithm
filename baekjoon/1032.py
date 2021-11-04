n = int(input())
stl = list()
for i in range(n):
    stl.append(input())

l = len(stl[0])
pattern_len = 0
dont = "False"

for i in range(l):

    for j in range(n):
        if stl[0][i] != stl[j][i]:
            dont = "True"
            break
    if dont == "True":
        break
    pattern_len += 1

result = ""

for i in range(pattern_len):
    result += stl[0][i]

for i in range(l - pattern_len):
    result += "?"

print(result)
