# 공주 구하기
from collections import deque
n, k=map(int, input().split())
dq=list(range(1, n+1))
dq=deque(dq)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()

# # 내 풀이
# n, k=map(int, input().split())
# a=list(range(1, n+1))
# tmp=0
# for i in range(n-1):
#     t=a.pop((tmp+k-1)%len(a))
#     tmp=(tmp+k-1)%(len(a)+1)
# print(a[0])
