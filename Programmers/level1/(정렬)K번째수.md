> https://programmers.co.kr/learn/courses/30/lessons/42748

## 문제
![](https://images.velog.io/images/suasue/post/2c9e43be-b692-443b-a6c5-bbbccea46654/image.png)

## 나의 풀이
```python
def solution(array, commands):
    res = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1] 
        c = commands[i][2] 
        new_array = sorted(array[a-1:b])
        res.append(new_array[c-1])
    return res
```

## 다른 사람의 풀이
```python
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]
```
리스트 컴프리헨션을 사용해서 `commands`의 값을 `a, b, c`로 한꺼번에 불러낼 수 있다는 것을 알았다! 언패킹!!

```python
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
```
비슷하게 언패킹을 활용했는데 이게 가독성이 좀 더 좋다.

```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```
`map`과 `lambda`식을 활용해서 풀 수도 있다!