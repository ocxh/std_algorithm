s = input()
s = s.replace(" ", "")
arr = list(s)

isU = 0
isC1 = 0
isP = 0
isC2 = 0

for i in range(len(arr)):
    offset = arr[i]
    if isU == 0:
        if arr[i] == "U":
            isU = 1
    elif isU == 1 and isC1 == 0:
        if arr[i] == "C":
            isC1 = 1
    elif isC1 == 1 and isP == 0:
        if arr[i] == "P":
            isP = 1
    elif isP == 1 and isC2 == 0:
        if arr[i] == "C":
            isC2 = 1

if isU and isC1 and isP and isC2:
    print("I love UCPC")
else:
    print("I hate UCPC")
