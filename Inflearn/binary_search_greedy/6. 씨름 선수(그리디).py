# 씨름 선수(그리디)
n=int(input())
body=[]
for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
body.sort(reverse=True) # 내림차순 정렬
largest=0
cnt=0
for x, y in body: # 최대값 찾는 방식을 쓰면 for문 하나로 할 수 있다.
    if y>largest:
        largest=y
        cnt+=1
print(cnt)

# 내 풀이
# n=int(input())
# Line=[]
# for _ in range(n):
#     Line.append(list(map(int, input().split())))
# cnt=0
# for x in Line:
#     for y in Line:
#         if x[0]<y[0] and x[1]<y[1]:
#             cnt+=1
#             break
# print(n-cnt)