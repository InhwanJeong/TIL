# Mysql 함수 및 쿼리

### 검색 결과 합치기
- 검색결과 컬럼 합치기
```mysql
select lon, lat from test
# lon lat
#  1  2
#  2  2
#  3  2

select concat(lon, ',', lat) as location from test
# location
# 1,2
# 2,2
# 3,2  
```

- 검색결과 여러열을 한행으로 합치기
```mysql
select group_concat(lat) as result from test
# result
# 2,2,2

select group_concat(lon) as result from test
# result
# 1,2,3
```

```mysql
SELECT petition_creat_id, model_name, model_ver, lon, lat, 
(select group_concat(object_name) from civil_comple_info) as object_name
FROM civil_con_req_decision_info;
```