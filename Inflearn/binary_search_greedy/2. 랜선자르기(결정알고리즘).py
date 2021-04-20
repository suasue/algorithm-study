# 랜선자르기(결정알고리즘)
'''
이분 검색은 결정알고리즘에서 사용한다.
결정알고리즘의 특징은 찾고자 하는 값이 특정 범위에 있다는 것을 알 수 있다.
답이 되는지 확인하는 함수를 만들어서 범위를 좁혀가며 푼다.
'''

def Count(len): # 그 길이로 만들 수 있는 랜선 갯수를 리턴 
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0 # 최대값
largest=0 # 가장 긴 랜선을 찾기 위한 변수
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1 # n개의 랜선 한 개의 길이는 1~가장 긴 것의 길이
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1 # 더 좋은 답을 찾아나간다
    else: # 길이가 너무 길어서 답이 안 될 경우
        rt=mid-1 # 긴 쪽을 버린다
print(res)