# 최대힙
import heapq as hq # heapq는 기본적으로 최소힙으로 작동한다. 최대힙으로 하려면 입력할 때 부호를 바꾼다.
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a)) # 출력할 때 원래 부호로 바꿈
    else:
        hq.heappush(a, -n) # 넣을 때 부호를 바꿔서 넣으면 최대힙 효과