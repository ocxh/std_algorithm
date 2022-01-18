# 선택정렬 알고리즘
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    # 리스트 전체중 가장 작은 값의 인덱스를 min_index에 담는다
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    # 맨 앞의 값과 가장 작은 값의 위치를 바꾼다
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
