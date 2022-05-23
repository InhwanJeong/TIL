## Unified Process(UP)

### 1. 요구사항 분석 
- 유스케이스 모델
    - 유스케이스 다이어그램
      - 액터 식별(액터)
      - 시스템 기능 식별(유스케이스)
    - 고수준 유스케이스(모든 유스케이스 작성 - 요구분석 단계)
    - 확장 유스케이스 (일부 유스케이스 작성 - 요구분석 단계)
- 도메인 모델(개념수준 클래스 다이어그램)
  - 개념적 클래스 식별
  - 연관 식별(클래스간)
  - 애트리뷰트 작성
- 시스템 순차 다이어그램(행위)(확장유스케이스 다음 작업)
- 시스템 오퍼레이션(클래스 메소드를 정의)
- 시스템 오퍼레이션 정의(메소드 간 연결)
  
### 2. 설계
- 통신 다이어그램(명세 수준 클래스 다이어그램)
- 클래스 다이어그램
  - GRASP(General Responsibility Assignment Software Patterns) 패턴 적용
    - Information Expert, Creator, Low Coupling 등
  - GoF(Gang of Four) 디자인 패턴 적용
    - 싱글톤 패턴, 옵저버 패턴, 스트레티지 패턴 등

---

UP 프로세스 종료

---

### 3. 구현
- TDD(Test-Driven-Development)
- BDD(Behavior-Driven-Development)
- DDD(Domain-Driven-Development)

### 4. 테스트
- 단위테스트
- 통합테스트
- end To end 테스트

### 5. 유지보수
- 리펙토링