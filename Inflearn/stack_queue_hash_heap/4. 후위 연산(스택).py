# 후위식 연산
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)        
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)        
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])        

# # 내 풀이
# a=input()
# stack=[]
# for x in a:
#     if x.isdecimal():
#         stack.append(x)
#     else:
#         p1=int(stack.pop())
#         p2=int(stack.pop())
#         if x=='+':
#             stack.append(p2+p1)
#         elif x=='-':
#             stack.append(p2-p1)
#         elif x=='*':
#             stack.append(p2*p1)
#         elif x=='/':
#             stack.append(p2/p1)
# res=stack.pop()
# print(res)