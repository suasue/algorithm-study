# 회문 문자열 검사
# 방법1 : 직접 검사
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
# 방법2 : 파이썬스러운 방법이나 방법1로 푸는 게 좋음
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))


# 숫자만 추출
s=input()
res=0
for x in s:
    if x.isdecimal(): # isdecimal : 0-9까지 숫자, isdigit : 알파벳이 아닌 모든 숫자 형태(2의 2승)
        res=res*10+int(x)
print(res)
cnt=0 # 약수의 개수 구하기 위해
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)


# 카드 역배치
a=list(range(21))
for _ in range(10):
    s, e=map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i]
a.pop(0) # 0 제거
for x in a:
    print(x, end=' ')
    
    
# 두 리스트 합치기
'''
파이썬에서는 +로 리스트를 합치고 sort를 사용할 수도 있으나.
sort 함수를 호출하면 시간복잡도가 nlogn이다.
반면, 이미 정렬되어 있다는 것을 활용하면 n번만 해도 된다. 
'''
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')