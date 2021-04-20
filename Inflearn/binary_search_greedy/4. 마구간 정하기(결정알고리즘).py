# 마구간 정하기(결정알고리즘)
def Count(len):
    cnt=1
    ep=Line[0] # 말이 마지막에 배치된 지점, 초기값으로 첫번째 마굿간에 첫번째 말 배치
    for i in range(1, n):
        if Line[i]-ep>=len: # 마지막 배치한 지점과 현재 배치하려는 지점 사이의 거리
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

# 내 풀이
# def Count(distance): # 배치할 수 있는 말의 개수
#     cnt=1
#     sum=0
#     for i in range(1, len(m)):
#         d=m[i]-m[i-1]
#         if sum+d>=distance:
#             cnt+=1
#             sum=0
#         else:
#             sum+=d
#     return cnt

# n, c=map(int, input().split())
# m=[]
# for _ in range(n):
#     tmp=int(input())
#     m.append(tmp)
# m.sort()
# print()
# lt=1 # 가장 가까운 거리가 될 수 있는 값
# rt=m[-1] # 가장 먼 거리가 될 수 있는 값
# res=0
# while lt<=rt: # 가장 가까운 두 말의 최대 거리 구하기
#     mid=(lt+rt)//2 
#     if Count(mid)>=c:
#         res=mid
#         lt=mid+1
#     else:
#         rt=mid-1
# print(res)