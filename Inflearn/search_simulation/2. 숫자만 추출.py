# 숫자만 추출
s=input()
res=0
for x in s:
    if x.isdecimal(): # isdecimal : 0-9까지 숫자, isdigit : 알파벳이 아닌 모든 숫자 형태(2의 2승)
        res=res*10+int(x)
print(res)
cnt=0 # 약수의 개수 구하기 위해
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)
