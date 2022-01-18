arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 인덱스0은 정렬되어있다고 가정. 인덱스1부터
for i in range(1, len(arr)):
    # 자신(i)보다 인덱스가 낮은 모든 값들과 비교 이동
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:  # 자기보다 작은 데이터를 만나면 멈춤
            break

print(arr)
