### 날짜 함수
- 날짜 데이터 검색 예시
```mysql
#기본시간 형식 "2021-03-24 09:26:25"
SELECT NOW();
 
#날짜만 "2021-03-24"
SELECT DATE(NOW());
 
#시간만 "09:26:25"
SELECT TIME(NOW());
 
#년도만 "2021"
SELECT YEAR(NOW());
 
#월만 "3"
SELECT MONTH(NOW());
 
#날짜만 포맷지정 "2021/03/24"
SELECT DATE_FORMAT(NOW(), '%Y/%m/%d');
 
#시간만 포맷지정 "09 26 25"
SELECT DATE_FORMAT(NOW(), '%H %i %s');
```

- 날짜 데이터 조건 예시
```mysql
#최근 하루
SELECT * FROM table_a WHERE create_dt BETWEEN DATE_ADD(NOW(), INTERVAL -1 DAY ) AND NOW();
 
#최근 일주일
SELECT * FROM table_a WHERE create_dt BETWEEN DATE_ADD(NOW(), INTERVAL -1 WEEK ) AND NOW();
 
#최근 한달
SELECT * FROM table_a WHERE create_dt BETWEEN DATE_ADD(NOW(), INTERVAL -1 MONTH ) AND NOW();
 
#특정 날짜 지정 방법1(2021년 3월 24일)
SELECT * FROM table_a WHERE create_dt >= '2021-03-24 00:00:00' AND create_dt <= '2021-03-25 00:00:00';
 
#특정 날짜 지정 방법2(2021년 3월 24일)
SELECT * FROM table_a WHERE DATE_FORMAT(create_dt, '%Y-%m-%d') = '2021-03-24';
 
#날짜 조건
SELECT * FROM table_a WHERE DATE(create_dt) BETWEEN '2020-01-01' AND '2020-12-31';
SELECT * FROM table_a WHERE DATE(create_dt) >= '2020-01-01' AND DATE(a.create_dt) <= '2020-12-31';
 
#월별 조건
SELECT * FROM table_a WHERE DATE_FORMAT(create_dt, '%Y-%m') BETWEEN '2021-01' AND '2021-03';
```