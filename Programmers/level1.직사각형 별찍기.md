> https://programmers.co.kr/learn/courses/30/lessons/12969

## 문제
![](https://images.velog.io/images/suasue/post/321d7802-fa3e-4a5b-8e09-b9a5daf99118/1.png)

## 나의 풀이
### 코드
```python
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print("*", end="")
    print()
```

### 설명
range와 for문의 중첩루프를 활용하여 풀었다. 
바깥쪽 루프가 세로 길이(b)이고, 안쪽 루프가 가로 길이(a)라는 것이 헷갈렸다. 