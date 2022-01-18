arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 0부터 최대값가지의 리스트 선언
count = [0] * (max(arr) + 1)

# count에 해당하는 인덱스에 숫자기록
for i in range(len(arr)):
    count[arr[i]] += 1

# count에 카운팅된 숫자만큼 0~ 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
