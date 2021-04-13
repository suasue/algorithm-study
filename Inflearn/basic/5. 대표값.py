# 대표값
n=int(input())
a=list(map(int, input().split()))
ave=round(sum(a)/n)
min=2147000000 # 정수형 중 가장 큰 값
for idx, x in enumerate(a):
    tmp=abs(ave-x) # 평균과 학생 점수의 거리
    if tmp<min:
        min=tmp
        score=x # 점수
        res=idx+1 # 학생의 실제 번호
    elif tmp==min: # 거리가 같을 때 큰 점수 선택
        if x>score:
            score=x
            res=idx+1
print(ave, res)

'''
대표값 문제 오류 수정
round는 round_half_even 방식을 택한다. round_half_up 방식X
'''
a=4.5000
print(round(a)) # 4, 정확히 중간이면 짝수 쪽으로
a=5.5000
print(round(a)) # 6
# 대안
a=66.5
a=a+0.5
a=int(a)
print(a)