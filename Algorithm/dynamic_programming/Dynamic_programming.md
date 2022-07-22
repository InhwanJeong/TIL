# 동적 계획법(Dynamic Programming)
- subproblems
- Topdown: 리커시브를 활용한 DP
  - 리커시브는 stack limit가 존재하기 때문에 모든곳에 적용할 수 없음.
- bottom up: 
- DP array, DP Table
- space Complexity Opt
- KnapSack problems
- 메모리(공간)를 활용한 속도 향상 

## 적용조건
- 문제가 서브 문제로 분할이 가능한가?
- 서브 문제들이 솔루션으로 더 큰 솔루션을 구할 수 있는가?
- 서브 문제들이 겹치는가?
  - 메모이제이션


## 시간복잡도, 공간복잡도
- O(2의 n승) -> O(n)으로 줄일 수 있음
  - 공간 복잡도도 O(n)을 가짐, 하지만 이전 데이터가 필요없다면 데이터를 삭제하면서 공간을 절약할 수 있음
  - 

## 문제 풀이 방법
- 최초의 f(0), f(1)... 을 구한다.
- 반복되는 수열을 구한다.
- 

