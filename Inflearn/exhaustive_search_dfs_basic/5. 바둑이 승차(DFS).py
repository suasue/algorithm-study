# 바둑이 승차(DFS)
# 부분집합 사용
# 시간 초과 버전(cut 해야 함!)
def DFS(L, sum): # L은 a에 접근하는 index 번호, sum은 부분집합의 합
    global result
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    DFS(0, 0)
    print(result)

# 개선 버전(Cut-Edge Tech)
# 바둑이의 총합 total을 미리 구해놓는다. 
# 부분집합에 더하든 안더하든 판단을 한 바둑이는 tsum에 무조건 더한다.
# total-tsum = 적용한 바둑이의 무게를 총합에서 뺀 것이므로, 앞으로 적용을 해야할 바둑이들의 무게
# sum + (total-sum)
def DFS(L, sum, tsum): # L은 a에 접근하는 index 번호, sum은 부분집합의 합
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0, 0, 0)
    print(result)


# # 내 풀이(60점 시간 초과)
# largest=0
# def DFS(L, sum):
#     global largest
#     if L==n:
#         if sum<=c and sum>largest:
#             largest=sum
#     else:
#         DFS(L+1, sum+a[L])
#         DFS(L+1, sum)

# if __name__=="__main__":
#     c, n=map(int, input().split())
#     a=[int(input()) for i in range(n)]
#     DFS(0, 0)
#     print(largest)