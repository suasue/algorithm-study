> https://programmers.co.kr/learn/courses/30/lessons/12954

## 문제
![](https://images.velog.io/images/suasue/post/b2bc8087-eb65-446e-ba39-a1772690fc9f/%EC%BA%A1%EC%B2%98.PNG)

## 나의 풀이
### 코드
```python
def solution(x, n):
    return [i*x for i in range(1, n+1)]
```

### 설명
리스트 표현식으로 풀었다.

1차 시도에는 아래와 같이 식을 작성했으나 런타임 에러가 났다. 
```python
def solution(x, n):
    return [i for i in range(x, n*x+1, x)]
```
생각해보니 x의 값이 음수일 때와 0일 때는 적용되지 않는다는 것을 발견했다. 하지만, 0보다 클 때, 0보다 작을 때, 0일 때 구분해서 작성하려고 하니 너무 복잡해지는 것 같아서 다시 한 번 고민해보았다. 

입출력 예를 살펴보니 리스트 요소의 개수가 n개이다. 그래서 먼저 1부터 n까지 하나씩 늘어나는 range를 생성하고, 식 부분에 x를 곱해주었다. 이렇게 x의 값에 상관없이 적용되는 리스트 표현식을 만들 수 있었다. 

## 다른 사람의 풀이(1)
```python
def solution(x, n):
    return [i * x + x for i in range(n)]
```
다른 사람의 풀이를 보니 간단하게 range(n)을 생성하고, 앞쪽의 식에서 나머지 처리를 해주었다.

## 다른 사람의 풀이(2)
```python
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x+(x*i))
    return answer
```

```python
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        InputValue = x*i
        print(InputValue)
        answer.append(InputValue)
    return answer
```
값을 담을 수 있는 빈 리스트 answer를 선언한다. for 반복문을 통해 1번째부터 n번째 값을 리스트에 차례로 넣는다.