# 응급실
from collections import deque
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q): # any 단 한 개라도 참이면
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break

# 내 풀이(못 품)
# from collections import deque
# n, m=map(int, input().split())
# a=list(map(int, input().split()))
# cnt=0
# a=deque(a)
# while a:
#     for _ in range(n):
#         if max(a)==a[0]:
#             a.popleft()
#         else:
#             cur=a.popleft()
#             a.append(cur)
#         print(a)