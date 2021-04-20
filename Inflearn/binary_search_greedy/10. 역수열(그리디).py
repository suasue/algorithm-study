# 역수열(그리디)
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x, end=' ')

# 내 풀이
# n=int(input())
# a=list(map(int, input().split()))
# tmp=[]
# for i in range(n, 0, -1):
#     tmp.insert((n-i)-a[i-1], i)
# tmp=tmp[::-1]
# for x in tmp:
#     print(x, end=' ')