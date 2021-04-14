# 봉우리
dx=[-1, 0, 1, 0] # 상하좌우 비교할 때는 이 리스트를 생성
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt=0
for i in range(1, n+1): # 가장자리는 돌면 안되므로 1부터 시작
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)

# 내 풀이
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# for x in a:
#     x.insert(0, 0)
#     x.append(0)
# a.insert(0, [0]*(n+2))
# a.append([0]*(n+2))
# cnt=0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1]:
#             cnt+=1
# print(cnt)