# 쇠막대기(스택)
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':            
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)     
       
# # 내 풀이
# a=list(input())
# stack=[]
# res=0
# for i in range(len(a)):
#     if a[i]=="(":
#         stack.append(a[i])
#     if a[i]==")" and a[i-1]=="(":
#         stack.pop()
#         res+=len(stack)
#     elif a[i]==")":
#         stack.pop()
#         res+=1
# print(res)