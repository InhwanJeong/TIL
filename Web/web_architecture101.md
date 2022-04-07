# web architecture 101

### 1. DNS
- Domain Name System, www를 가능하게 해주는 기술

### 2. Load Balancer
- horizontal scaling(수평적 스케일링)
    - 컴퓨터의 개수를 늘림
    - 웹개발에서 거의 항상 수평적 스케일링을 선호함
        - 기기는 고장이 나기 때문
        - 네트워크 오류와 성능 저하에 대비가 가능함.
    - 각기 다른 서버에서 구동함으로서 백엔드 서비스의 결합도를 줄여줌
    
- vertical scaling
    - 컴퓨터의 성능을 높힘
    

### 3. web Application Severs
- MVC 웹서버
- API 서버와 정적 컨텐츠를 처리하는 웹 서버

### 4. Database Severs
- 하나 혹은 이상의 데이터베이스를 활용하여 정보를 저장
- SQL은 수평 스케일링이 힘들다. 

### 5. Caching Service
- O(1) 시간안에 찾아볼 수 있는 Key/Value data store를 제공한다.
- 비싼 연산의 결과를 저장하여 활용한다.
    - ex) 하루에 한번 바뀌는 배너
    - ex) 누적 방문횟수 등
    - ex) 구글은 흔한 검색 결과는 캐싱해둠
    - ex) facebook은 post data, 친구목록 등과 같이 로그인 했을 때 보여지는 많은 정보를 캐싱함
    
### 6. Job Queue & Servers
- 비동기 작업을 가능하게 해주는 여러 아키텍처 중 보편적인 방법
- job 이 들어가는 queue와 job을 수행하는 servers(workers)로 구성되어 있음

### 7. Full-text Search Service
- 사용자가 어떤 text input를 입력하면 가장 연관된 결과를 반환하는 기능
- inverted index를 활용하여 검색어를 포함하고 있는 문서들을 빠르게 검색한다.
- MySQL은 full-text search를 지원한다.
- Elasticsearch가 가장 대표적인 서비스이다.

### 8. Service
- 일정 크기 이상의 서비스들은 분리가 되어야함
    - Account
    - Payment
    - Content
    
### 9. Data
- data pipeline, 데이터 수집, 저장, 분석
    - app이 사용자와 상호작용한 데이터를 "firehose"에 전송한다. 일반적으로 raw data는 변환되거나 추가되서 저장됨. AWS kinesis나 Kafka가 있다.
    - raw data와 변형/추가된 데이터는 cloud storage에 저장된다.
    - 변형/추가된 데이터는 분석을 위해 data warehouse에 올라간다. AWS Redshift, Oracle등 사용. 데이터 규모가 크다면 Hadoop과 같은 NoSQL MapReduce기술을 사용하기도 한다.
    
### 10. Cloud Storage
- 동영상, 오디오, 사진, CSS, javascript 등을 저장

### 11. CDN
- Content Delivery Network
- HTML, CSS, Javascript와 같은 정적 파일을 여러 edge 서베에 걸쳐 분산하여 사용자들이 edge 서버에서 다운로드 받을 수 있도록 함.