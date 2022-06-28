## 데이터 엔지니어
- 데이터가 원활하게 흐를 수 있도록 하는 직업(자동화된 데이터 처리)
  - 데이터 분석을 더 쉽게할 수 있는 환경(인프라) 구축
  - 상황에 따라 table 10개 이상을 join할 수 있음
  
- 데이터를 이용하는 목적
  - BI(Business Intelligence): 기업의 업적 등을 수집해서 경영상의 의사결정에 도움을 줌
  - 데이터 마이닝: 통계분석과 머신러닝 등 알고리즘을 사용하여 데이터로부터 가치 있는 정보를 발견하는 것

- ETL 파이프라인
    - Extract: 데이터 추출
      - db 또는 웹, 앱 로그 데이터 추출
    - Transform: 데이터 변환
        - 데이터를 잘 활용할 수 있도록 변환
    - Load: 데이터 적재
        - 변환한 데이터 사용할 수 있도록 설정
- 데이터 처리 방식
    - 배치(batch): 1시간 1번, 1일에 한번 등 특정 시간에 1번 실행하는 방식
    - 실시간(realtime, streaming): 요청시 바로 처리
    
- 데이터 마트(data mart) 구축
    - SQL Join 결과를 Batch로 Table에 저장
    - 특정 목적, 도메인에 맞는 마트 구축
  
- BI(Business Intelligence) 도구
    - Tableau, redash, superset, metabase
    - 데이터 마트와 시각화 도구를 결합하는 환경 마련
    
- Data Product: 사내 구성원들을 위한 data product 개발
    - 분석도구
    - 데이터 로그 시스템
    - 머신러닝/딥러닝 시스템

### 데이터베이스를 사용하지 않는 이유
- 데이터 분석을 위한 쿼리는 데이터베이스에 무리를 줄 수 있음
- 서비스를 위한 데이터베이스는 장애가 나면 안됨
- 따라서 데이터베이스보다 Data warehouse에 데이터를 저장하는 추세
- 데이터 웨어하우스
    - 데이터 분석에 특화된 DB
    - GCP의 bigquery, aws의 redshift, snowflake
    

### 데이터 엔지니어 역량
- 대용량처리, DB, 네트워크
- 개발 역량(Python, java, scala, shell, docker, go)
- 클라우드, Docker, 쿠버네티스
- 데이터 아키텍처 설계 역량
- apache spark, apache kafka: 대용량 데이터 처리, 실시간 처리
- apache airflow: 워크 플로우 관리, crontab 대안으로 사용

### 하둡 vs nosql
- nosql: rdb로 취급할 수 없을만큼 대량의 데이터를 처리
- 하둡(Hadoop): 다수의 컴퓨터에서 대량의 데이터를 처리하기 위한 시스템
