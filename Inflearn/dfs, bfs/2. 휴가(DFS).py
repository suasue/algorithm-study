# 휴가
def DFS(L, sum):
    global res
    if L==n+1: # 종료지점은 딱 n+1이어야 함
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1: # 날짜를 넘어서면 안 됨
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum) # 상담 안 할 거면 그냥 하루 넘어감

if __name__="__main__":
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.insert(0, 0) # 인덱스 번호를 날짜로 하기위해 한 칸씩 밈
    P.insert(0, 0)
    DFS(1, 0) # L이 날짜(인덱스)
    print(res)