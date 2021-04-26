# 부분집합 구하기(DFS)
# DFS를 잘 하려면 상태트리를 잘 구성해야 함. 그리고 상태트리에 대해서 재귀를 호출하면 됨.
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1 # 체크가 들어가면 해당 원소를 부분집합으로 사용 
        DFS(v+1)
        ch[v]=0 # 사용하지 않겠다
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1) # 원소를 사용하는지 여부 알리는 체크 변수 지정
    DFS(1)