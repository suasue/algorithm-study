# 회의실 배정(그리디)
n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))
et=0 # 끝나는 시간 기록, endtime
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)

# 내 풀이
# n=int(input())
# a=[]
# for _ in range(n):
#     a.append(list(map(int, input().split())))
# a=sorted(a, key=lambda x:x[1]) # 끝나는 시간으로 정렬
# cnt=1
# tmp=a[0]
# for x in a:
#     if x[0]>=tmp[1]: 
#         tmp=x
#         cnt+=1
# print(cnt)