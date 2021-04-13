# 정다면체
n, m=map(int, input().split())
cnt=[0]*(n+m+3) # 0으로 초기화된 cnt 리스트 생성
max=-2147000000
for i in range(1, n+1):
    for j in range(1, m+1): # 카운팅
        cnt[i+j]+=1
for i in range(n+m+1): # 최대값 구하기
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1): # 최대값을 가진 숫자 구하기
    if cnt[i]==max:
        print(i, end=' ')