# 증가수열 만들기(그리디)
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], "L"))
    if a[rt]>last:
        tmp.append((a[rt], "R"))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=="L":
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(res)

# 내 풀이
# n=int(input())
# a=list(map(int, input().split()))
# cnt=0
# tmp=0
# s=""
# for i in range(n):
#     if min(a[0], a[-1])==a[0] and a[0]>tmp or a[0]>tmp and a[-1]<=tmp:
#         s+="L"
#         tmp=a.pop(0)
#         cnt+=1
#     elif min(a[0], a[-1])==a[-1] and a[-1]>tmp or a[-1]>tmp and a[0]<=tmp:
#         s+="R"
#         tmp=a.pop()
#         cnt+=1
# print(cnt)
# print(s)
