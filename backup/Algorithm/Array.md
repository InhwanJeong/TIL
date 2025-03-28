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
  

### 배열의 특정 연속된 구간을 처리하는 경우
- 투 포인터(Two Pointers)
  - N개의 자연수로 구성된 수열, 합이 M인 연속된 수열의 개수는?
  - O(N)시간만에 풀어야 함 
- 구간 합(Prefix Sum)