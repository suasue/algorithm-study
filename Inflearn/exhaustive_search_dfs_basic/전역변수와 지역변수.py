# 전역변수와 지역변수
def DFS1():
    cnt=3
    print(cnt) # 지역변수 이름공간에 cnt가 있는지 먼저 확인. 만약 없으면 전역변수 이름공간에서 찾는다. 

def DFS2():
    global cnt
    if cnt==5:
        cnt=cnt+1 # global이 있으므로 cnt를 지역변수로 선언되지 않는다.
        print(cnt)

if __name__=="__main__":
    cnt=5 # main 스크립트에 선언되면 전역변수, 모든 함수가 다 접근할 수 있고, 값도 변경할 수 있음.
    DFS1()
    DFS2()
    print(cnt)

# 리스트도 값을 바꾸는데 지역변수화되지 않고 전역변수로 남는가?
def DFS():
    a[0]=7 # 여기서 a는 전역리스트, 새로운 지역리스트를 만드는 건 아님.
    # a=[7] # 여기서 a는 지역리스트
    # global a # 이거 해주면 아래에서 에러 안 뜸!
    # a=a+[4] # 이렇게 하면 에러가 뜸. a= 하면 지역리스트를 만들겠다고 언어번역이 됨. 근데 a가 할당이 안 되어 있음
    print(a)

if __name__=="__main__":
    a=[1, 2, 3]
    DFS()
    print(a)