# k번째 약수
n, k=map(int, input().split())
cnt=0 # 개수를 세야 하니까
for i in range(1, n+1):
    if n%i==0: # 나머지가 0일 때, i가 n의 약수일 때
        cnt+=1
    if cnt==k: # 약수의 개수가 k개일 때
        print(i)
        break
else: # for문에서 break를 당하지 않고 정상적으로 끝난다면
    print(-1)