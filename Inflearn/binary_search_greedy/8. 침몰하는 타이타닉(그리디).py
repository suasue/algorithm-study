# 침몰하는 타이타닉(그리디)
from collections import deque

n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)

# 내 풀이(틀림) -> 다시 풀기
# n, m=map(int, input().split())
# a=list(map(int, input().split()))
# a.sort()
# print(a)
# cnt=0
# for i in range(len(a), 0):
#     for j in range(len(a)):
#         cnt+=1
#         tmp=-1
#         largest=a[i]
#         if a[i]+a[j]<=m and a[i]+a[j]>largest:
#             largest=a[i]+a[j]
#             tmp=j
#         a.pop()
#         if tmp>0:
#             a.pop(tmp)
# print(cnt)