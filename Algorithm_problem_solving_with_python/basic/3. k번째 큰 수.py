# K번째 큰 수
n, k=map(int, input().split())
a=list(map(int, input().split()))
res = set() # 중복 제거
for i in range(n): # 3중 for문
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res) # set에는 sort기능이 없다
res.sort(reverse=True)
print(res[k-1])