# 합이 같은 부분집합(DFS)
def DFS(L, sum):
    if sum>total//2: # 속도 단축
        return
    if L==n: # 0번부터 시작했으니
        if sum==(total-sum):
            print("YES")
            sys.exit(0) # 프로그램 종료
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")

# # 내 풀이
# def DFS(v):
#     b=[]
#     if v==n+1:
#         for idx, val in enumerate(a):
#             if ch[idx]==1:
#                 b.append(val)
#         if sum(list(set(a)-set(b)))==sum(b):
#             print("YES") # 설명보고 추가
#             sys.exit(0)
#     else:
#         ch[v-1]=1
#         DFS(v+1)
#         ch[v-1]=0
#         DFS(v+1)

# if __name__=="__main__":
#     checked=0
#     n=int(input())
#     a=list(map(int, input().split()))
#     ch=[0]*(n+1)
#     DFS(1)
#     print("NO") # 설명보고 추가
