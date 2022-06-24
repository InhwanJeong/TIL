# list
- 리스트는 스택으로 사용할 수 있음(append, pop)
```python
test = []

# 리스트 마지막 위치에 항목 추가
# a[len(a):] = [x]
test.append("x")

# 리스트 확장
test.extend()

# 주어진 위치에 값 삽입
test.insert(0, "y")

# 리스트 마지막 값 삭제
test.pop()

# 리스트 값 삭제 - 가장 첫번째에 있는 해당 값
test.remove("x")

# 특정 인덱스 값 지우기
del test[1]

# 리스트 내용 비우기
test.clear()

# x가 등장하는 횟수 리턴
test.count("x")

# 리스트 인덱스 반대로 변환
test.reverse()

# 리스트 사전순으로 정렬
test.sort()
```

## list 예제
```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') # 2

# banana를 4 위치(kiwi부터 시작) 이후에 나오는 첫번째 바나나 index를 반환
fruits.index('banana', 4)  # 6

# orange apple pear banana kiwi apple banana
print(" ".join(fruits))
```

## list comprehensions
```python
squares = []
for x in range(10):
    squares.append(x**2)

print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

# set

# dictionary
- 별 표현식(star expression)
```python
a, b, *c = (0, 1, 2, 3, 4, 5) # a, b, *c = [0, 1, 2, 3, 4, 5]
print(c) #[2, 3, 4, 5]
```
