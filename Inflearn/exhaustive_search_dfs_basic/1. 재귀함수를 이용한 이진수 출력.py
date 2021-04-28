# 재귀함수를 이용한 이진수 출력
def DFS(x):
    if x==0:
        return # 함수 종료
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    n=int(input())
    DFS(n)

# # 내 풀이
# n=int(input())
# def divide(n):
#     if n//2>0:
#         divide(n//2)
#     print(n%2, end='')
# divide(n)