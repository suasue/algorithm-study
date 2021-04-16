# 격자판 회문수
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)

# 내 풀이
# a=[list(map(int, input().split())) for _ in range(7)]
# cnt=0
# for i in range(7):
#     for j in range(3):
#         for k in range(2):
#             if a[i][j+k]!=a[i][j+4-k]:
#                 break
#         else:
#             cnt+=1
#         for k in range(2):
#             if a[j+k][i]!=a[j+4-k][i]:
#                 break
#         else:
#             cnt+=1
# print(cnt)