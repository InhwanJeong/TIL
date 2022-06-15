## insert 문
- 기본형태
```
INSERT INTO table_name(c1,c2,...)
VALUES(v1,v2,..);
```

- select문 혼합형 - 통째로 복사
```
INSERT INTO table_name(column_list)
SELECT 
   select_list 
FROM 
   another_table
WHERE
   condition;
```

- select문 혼합형 - 일부분만 복사
```
INSERT INTO suppliers (
    supplierName, 
    phone, 
    addressLine1,
)
SELECT 
    customerName,
    phone,
    addressLine1,
FROM 
    customers
WHERE 
    country = 'USA' AND 
    state = 'CA';
```

- select문 혼합형 - 컬럼 1개 복사
```
INSERT INTO stats(totalProduct, totalCustomer, totalOrder)
VALUES(
	(SELECT COUNT(*) FROM products),
	(SELECT COUNT(*) FROM customers),
	(SELECT COUNT(*) FROM orders)
);
```

## 성능개선
- multi values
    - insert 되어야 할 데이터가 많을수록 속도가 엄청 빨라진다. 
```
INSERT INTO stats(test)
VALUES(1), (2), (3) ...;
```