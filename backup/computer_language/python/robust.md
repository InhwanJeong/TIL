## 프로그램 강건성(견고성)
- 오류가 발생해도 문제가 없도록 프로덕션화(productionize)해 코드에 방탄 처리를 해야한다.
- 규모 확장성, 성능


### try/except/else/finally의 블록을 잘 활용하라
- finally 블록
    - try에서 예외 발생 시 finally를 반드시 실행 후 에러를 반환한다.
    - try에서 예외 미 발생 시 finally를 반드시 실행 후 다음을 처리한다.
    - finally를 거치지 않고 에러를 발생 시켜야 한다면 try보다 먼저 코드를 작성하자.
    
- else 블록
    - 예외가 발생되지 않을 경우 실행되는 블록
    - try안에 들어간 코드를 최소화 할 수 있다.
    - 예외가 발생할 여지가 있는 코드 외 코드를 넣으면 가독성이 좋아진다.
    
- 정상처리(try, else, finally)
- 비정상 처리(try, except, finally)
