# 소수(에라토스테네스 체)
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1): # 2부터
    if ch[i]==0: # 소수일 때
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)