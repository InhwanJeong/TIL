# 알고리즘 정리

## 복잡도
- 시간복잡도(연산)
  - O(1) 상수시간 
  - O(n) 로그시간
  - O(n) 선형시간 
  - O(nlogn) 로그선형시간
  - O(n**2) 이차시간
  - O(n**3) 삼차시간
  - 연산 횟수가 10억이 넘어가면 C언어 기준 1초가 소요됨
  - N의 범위가 500 인경우 N**3으로 설계하면 풀 수 있음
  - N의 범위가 2,000 인경우 N**2으로 설계하면 풀 수 있음
  - N의 범위가 100,000 인경우 NlogN으로 설계하면 풀 수 있음
  - N의 범위가 10,000,000 인경우 N으로 설계하면 풀 수 있음

- 공간복잡도(메모리)
  - int a[1000]: 4KB
  - int a[1000000]: 4MB
  - int a[2000][2000]: 16MB
  - 일반적으로 128~512MB 정도로 제한 -> 데이터 개수가 1000만 단위를 넘어가면 안됨

- 파이썬 시간 측정
~~~python
import time
start_time = time.time()

end_time = time.time()
print("time: ", end_time-start_time)
~~~


## Array
- random access가 가능한 자료구조
  - e.g. num[0], num[2] 등
- sorting, O(nlogn)
  - unstable: 중복값 정렬시 위치를 지키지 않음
    - quick sort
    - heap sort
  - stable: 중복값 정렬시 해당 위치를 보장함
    - merge sort
- search, O(n)
- binary search, O(logn)
- 연관 기법
    - Dynamic Programming
    - BackTracking
    - graph (2D, 3D)
  
- sliding
  - sliding은 양의 정수를 가질 때만 사용할 수 있음
  