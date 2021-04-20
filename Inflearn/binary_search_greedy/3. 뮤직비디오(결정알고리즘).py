# 뮤직비디오(결정알고리즘)
def Count(capacity): # 어떤 용량 DVD가 모든 영상을 녹화하려면 몇 개 필요한지
    cnt=1 # 우선 DVD 한 장이 필요
    sum=0
    for x in Music:
        if sum+x>capacity: # x가 더해졌을 때 용량이 넘친다면 
            cnt+=1 # DVD 한 개가 더 필요하다. 
            sum=x # 그리고 새로운 DVD에는 x가 더해진다. -> 숨어있는 논리 : DVD의 용량은 어떤 노래보다도 크거나 같아야 한다.   
        else: # x가 더해졌을 때 용량이 괜찮다면
            sum+=x # 그 DVD에 x를 더한다. 
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music) # 최대 용량은 동영상 길이의 합이다. 
res=0 
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m: # DVD 하나의 용량은 가장 긴 노래보다 크거나 같아야 한다!
        res=mid # 위 조건을 만족한다면 mid는 답이 될 자격이 있다.
        rt=mid-1 # 최소 용량(=가장 좋은 조건)을 찾아간다. 
    else:
        lt=mid+1 # 용량을 키워야 한다. 
print(res)

# 내 풀이(틀림)
# Count 함수 로직 틀림
# def Count(a, size):
#     cnt=0
#     sum=0
#     for x in a:
#         sum+=x
#         if sum>=size:
#             cnt+=1
#             sum=0
#     return cnt+1

# n, m=map(int, input().split())
# a=list(map(int, input().split()))
# lt=1
# rt=sum(a)
# res=0
# while lt<=rt:
#     mid=(lt+rt)//2
#     if Count(a, mid)<=m:
#         res=mid
#         rt=mid-1
#     else:
#         lt=mid+1
# print(res)
