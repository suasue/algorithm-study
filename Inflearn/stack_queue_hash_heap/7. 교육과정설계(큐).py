# 교육과정설계
from collections import deque
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

# # 내 풀이(80점)
# from collections import deque
# req=list(input())
# n=int(input())
# for i in range(n):
#     x=list(input())
#     dq=deque(req)
#     for j in x:
#         if j==dq[0]:
#             dq.popleft()
#         if not dq:
#             print(f"#{i+1} YES")
#             break
#     else:
#         print(f"#{i+1} NO")    