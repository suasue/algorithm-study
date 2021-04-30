# 조합 구하기
def DFS(L, s):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*(n+1)
    cnt=0
    DFS(0, 1)
    print(cnt)
    
# 내 풀이
# def DFS(L, s):
#     global cnt
#     if L==m:
#         cnt+=1
#         for k in range(m):
#             print(res[k], end=' ')
#         print()
#     else:
#         for i in range(s, n+1): # 1, 2, 3, 4
#             res[L]=i
#             DFS(L+1, i+1)
            
# if __name__=="__main__":
#     n, m=map(int, input().split())
#     cnt=0
#     res=[0]*m
#     DFS(0, 1)
#     print(cnt)
    
    