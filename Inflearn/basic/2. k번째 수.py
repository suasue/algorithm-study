# k번째 수
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e] # s ~ e번째 사이로 a를 재할당
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))