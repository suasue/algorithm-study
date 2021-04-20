# 창고 정리
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort() # 정렬해서 맨 앞의 값과 맨 뒤의 값을 이용한다. 
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()
print(a[L-1]-a[0])

# 내 풀이(80점)
# l=int(input())
# a=list(map(int, input().split()))
# m=int(input())
# for i in range(m):
#     largest=-1247000000
#     smallest=1247000000
#     large_index=0
#     small_index=0
#     for j in range(1, l):
#         if a[j]>largest:
#             largest=a[j]
#             large_index=j
#         if a[j]<smallest:
#             smallest=a[j]
#             small_index=j
#     a[large_index]-=1
#     a[small_index]+=1
# print(largest-smallest)