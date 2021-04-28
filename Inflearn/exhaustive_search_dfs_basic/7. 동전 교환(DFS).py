# 동전교환
def DFS(L, sum):
    global res
    if L>res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    res=2147000000
    a.sort(reverse=True) # 큰 값부터 계산!
    DFS(0, 0)
    print(res)

# # 내 풀이(40점, 시간 초과)
# def DFS(L, sum):
#     global cnt
#     if sum>m:
#         return
#     if L>cnt and sum<m:
#         return
#     if sum==m:
#         cnt=L
#     else:
#         for i in range(n):
#             DFS(L+1, sum+a[i])
            
# if __name__=="__main__":
#     n=int(input())
#     a=list(map(int, input().split()))
#     m=int(input())
#     cnt=2147000000
#     DFS(0, 0)
#     print(cnt)