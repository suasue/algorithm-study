# 사과나무(다이아몬드)
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

# 내 풀이
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# tot=0
# cnt=0
# for i in range(n):
#     if i<=n//2:
#         tot+=sum(a[i][n//2-cnt:n//2+1+cnt])
#         cnt+=1
#     else:
#         cnt-=1
#         tot+=sum(a[i][n//2+1-cnt:n//2+cnt])
# print(tot)