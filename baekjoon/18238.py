li1 = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
li2 = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
li2.reverse()
li2.remove("A")
li2.insert(0, "A")
n = input()
count = 0

for i in range(len(n)):
    for j in range(len(li1)):
        if n[i] == li1[j]:
            buf1 = j
            print(j)
    for j in range(len(li2)):
        if n[i] == li2[j]:
            buf2 = j
            print(j)

    if buf1 <= buf2:
        count += buf1
    else:
        count += buf2

print(count)
# 푸는중
