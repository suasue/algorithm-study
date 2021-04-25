# 단어 찾기
# 딕셔너리 자료구조를 사용하면 편하게 풀 수 있다. 문자도 키깂으로 사용할 수 있다.
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
for key, value in p.items():
    if value==1:
        print(key)

# # 내 풀이
# n=int(input())
# a=[input() for _ in range(n)]
# b=[input() for _ in range(n-1)]
# for x in a:
#     if not (x in b):
#         print(x)