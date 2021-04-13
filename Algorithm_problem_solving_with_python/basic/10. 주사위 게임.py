# 주사위 게임
n=int(input())
res = 0
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c=map(int, tmp)
    if a==b and b==c: # 가장 좋은 조건부터
        money=10000+a*1000
    elif a==b or a==c: # b==c가 같은 경우는 따로, 왜냐면 a로 계산하기 위해
        money=1000+a*100
    elif b==c:
        money=1000+b*100
    else:
        money=c*100 # 정렬해둠
    if money>res:
        res=money
print(res)