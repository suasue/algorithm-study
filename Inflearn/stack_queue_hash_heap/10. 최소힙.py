# 최소힙
import heapq as hq
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a)) # heappop(a) : a에서 루트 노드값을 pop
    else:
        hq.heappush(a, n) # a라는 list에 n을 최소힙의 형태로 넣는다.
