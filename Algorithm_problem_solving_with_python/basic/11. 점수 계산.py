# 점수 계산
n=int(input())
a=list(map(int, input().split()))
sum=0
cnt=0 # 가중치 값
for x in a: # 1일 때는 가중치가 1씩 올라가면서 더해지는데
    if x==1:
        cnt+=1
        sum+=cnt
    else: # 아닐 때는 가중치가 0으로 초기화되서 시작
        cnt=0
print(sum)