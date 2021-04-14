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