> https://programmers.co.kr/learn/courses/30/lessons/43165

## 나의 풀이
### 코드
```python
def solution(numbers, target):
    answer = 0
    def DFS(level, num):
        nonlocal answer
        if level==len(numbers) and target==num:
            answer+=1
            return
        if level==len(numbers):
            return
        else:
            DFS(level+1, num+numbers[level])
            DFS(level+1, num-numbers[level])
    DFS(0, 0)
    return answer
```

### 설명
DFS를 사용해서 풀이함
global을 쓰면 왜 안 되고, nonlocal로 쓰면 왜 되는가?