# 아나그램
# 딕셔너리
a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
# 딕셔너리 개선코드
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if sH.get(x)>0:
        print("NO")
        break
else:
    print("YES")
# 리스트 해쉬, 아스키 코드
a=input()
b=input()
str1=[0]*52
str2=[0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")

# # 내 풀이
# a=input()
# b=input()
# tmp=dict()
# for x in a:
#     if x in tmp.keys():
#         tmp[x]+=1
#     else:
#         tmp[x]=1
# for x in b:
#     if x in tmp.keys():
#         tmp[x]-=1
#         if tmp[x]<0:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")