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
    

# k번째 수
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e] # s ~ e번째 사이로 a를 재할당
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))


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


# 최솟값 구하기
# 방법 1
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arr_min=float('inf') # 가장 큰 값으로 초기화

for i in range(len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]
print(arr_min)
# 방법 2 
arr_min=arr[0] # 0번째 값으로 초기화해도 됨
for x in arr: # for문에 len() 안 쓰고 바로 배열 사용해도 됨
    if x < arr_min:
        arr_min=x
print(arr_min)


# 대표값
n=int(input())
a=list(map(int, input().split()))
ave=round(sum(a)/n)
min=2147000000 # 정수형 중 가장 큰 값
for idx, x in enumerate(a):
    tmp=abs(ave-x) # 평균과 학생 점수의 거리
    if tmp<min:
        min=tmp
        score=x # 점수
        res=idx+1 # 학생의 실제 번호
    elif tmp==min: # 거리가 같을 때 큰 점수 선택
        if x>score:
            score=x
            res=idx+1
print(ave, res)

'''
대표값 문제 오류 수정
round는 round_half_even 방식을 택한다. round_half_up 방식X
'''
a=4.5000
print(round(a)) # 4, 정확히 중간이면 짝수 쪽으로
a=5.5000
print(round(a)) # 6
# 대안
a=66.5
a=a+0.5
a=int(a)
print(a)


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