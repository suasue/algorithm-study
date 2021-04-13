# 뒤집은 소수
n=int(input())
a=list(map(int, input().split()))
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1): # 소수는 자기 자신의 절반까지만 존재한다.
        if x%i==0:
            return False
    else:
        return True

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
