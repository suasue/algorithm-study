# 이분검색
n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort() # 이분검색의 전제 조건 - 정렬
lt=0
rt=n-1
while lt<=rt: # lt가 rt보다 크면 탐색을 다 한 것
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

# 내 풀이
# n, m=map(int, input().split())
# a=list(map(int, input().split()))
# a.sort() # 정렬
# lt=0
# rt=n-1
# while True:
#     mid=(rt+lt)//2
#     if a[mid]==m: 
#         print(mid+1)
#         break
#     elif m>a[mid]:
#         lt=mid+1
#     elif m<a[mid]:
#         rt=mid-1