> https://programmers.co.kr/learn/courses/30/lessons/12916

## 문제
![](https://images.velog.io/images/suasue/post/ecd615f0-7e60-423d-9ed8-3d1b039f860c/image.png)

## 나의 풀이
```python
def solution(s):
    return s.count('p') + s.count('P') == s.count('y') + s.count('Y')
```

## 다른 사람의 풀이
```python
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
```
문자열 전체를 먼저 소문자로 만들고 비교하면 편하다. 