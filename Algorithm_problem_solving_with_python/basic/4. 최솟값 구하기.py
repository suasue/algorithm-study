# 최솟값 구하기
# 방법 1
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arr_min=float('inf') # 가장 큰 값으로 초기화

for i in range(len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]
print(arr_min)
# 방법 2 
arr_min=arr[0] # 0번째 값으로 초기화해도 됨
for x in arr: # for문에 len() 안 쓰고 바로 배열 사용해도 됨
    if x < arr_min:
        arr_min=x
print(arr_min)