# 순열 구하기
# 중복 체크리스트 만들기! 중복일 때는 뻗지 못하도록 커트
def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0 # 1로 체크했던 것을 0으로 풀어준다.

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)

# 내 풀이
# def DFS(L):
#     global cnt
#     if L==m:
#         if len(res)==len(list(set(res))):
#             for j in range(m):
#                 print(res[j], end=' ')
#             print()
#             cnt+=1
#     else:
#         for i in range(1, n+1):
#             res[L]=i
#             DFS(L+1)

# if __name__=="__main__":
#     n, m=map(int, input().split())
#     cnt=0
#     res=[0]*m
#     DFS(0)
#     print(cnt)