## 인덱스(index)
- clustered index
  - 범위 검색에 좋음
  - 값 사이에 insert 할 떄 상당히 많은 자원 소모
- non-clustered index
  - 추가 저장공간 필요
  - insert 할 때 인덱스 생성 필요
- B-tree
- 테이블과 매핑된 또다른 테이블을 생성


### mysql
- 인덱스 생성전 검색(0.1초, 100만개)
  - 모든 행 스캔
  - select * from user where user_name='inan'
- 인덱스 생성
```
ALTER TABLE user ADD INDEX user_index(user_name)
```
- 인덱스 생성 후 검색(0.0027초, 100만개)
  - 정렬된 인덱스 컬럼에서 b-tree알고리즘을 통해 inan 단어 검색  
  - select * from user where user_name='inan'