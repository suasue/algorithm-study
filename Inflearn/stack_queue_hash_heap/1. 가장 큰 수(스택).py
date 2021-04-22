# 원리 : 자기 앞에 자기보다 작은 숫자가 나오면 안 된다.
# 스택 LIFO(Last In First Out), 파이썬에는 리스트 append, pop을 이용
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)
    
# # 내 풀이(실패)
# # 시도1
# a, m=map(int, input().split())
# a=list(map(int, str(a)))
# max_index=a.index(max(a[:m+1]))
# a=a[max_index:]
# for i in range(m-max_index):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a.pop(j+1)
#             break
# for x in a:
#     print(x, end='')

# # 시도2
# for i in range(m):
#     a.pop(a.index(min(a[:len(a)])))
# for x in a:
#     print(x, end='')
