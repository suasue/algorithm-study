# 자릿수의 합
# 방법 1 : 몫, 나머지
n=int(input())
a=list(map(int, input().split()))
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10 # x를 10으로 나눈 나머지를 더해준다
        x=x//10 # x는 10으로 나눈 몫으로 변한다
    return sum
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
# 방법 2 : str
n=int(input())
a=list(map(int, input().split()))
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)