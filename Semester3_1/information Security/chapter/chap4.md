## 1. 부호화
- 암호화에서 컴퓨터 사용이 필수
- 문자열을 비트로 대응 시키는 것

```
평문 -> 비트열 -> 암호화 -> 비트열
   부호화


문자열 midnight 비트열로 부호화

얻어낸 비트열을 XOR연산


비트열(평문) -> XOR -> 암호 -> XOR -> 평문

```

## 2. 일회용 패드 - 절대 해독 불가능한 암호
- OTP(one time password): 전사공격으로 절때 해독 불가
- 문자열이 복호화 되었다고 해도, 바른 평문인지 판정 할 수 없다.

#### 일회용 패드의 단점
- 키의 배송: 키를 안전하게 보낼 수 있는 방법이 있다면 평문 그 자체를 같은방법으로 안전하게 보낼 수 있을 것
- 키의 보존
- 키의 재이용: 과거에 사용한 랜덤한 비트열을 절대로 재이용해서는 안 된다.
- 키 동기화: 1비트라도 어긋나면 복호화 불가
- 키의 생성: 난수는 의사난수가 아닌 실제 난수여야 한다.

## 3. DES(data encryption standard)
- 1977년 미국의 연방 정보처리 표준 규격으로 채택된 대칭암호
- 현재 전사 공격으로 해독할 수 있는 수준

## 암호화/복호화
- 블럭 암호

```

Block cipher: 일정 값 단위로 잘라서 암호화를 한다.

|  64   |   64   |   64   |   64  |

stream cipher: 비트열이 들어 올 때마다 키 비트열을 만나  -> XOR -> 암호화

```

- 페이스텔 네트워크(교차되는 구조)
  - 페이스텔 구조, 암호
  - DES외 다른 암호도 채용
  - 여러개의 라운드로 구성
- 같은 서브 키로 페이스텔 네트워크를 2회 통과시키면 원래로 돌아간다.

#### 페이스텔 네트워크 특징
- 원하는 만큼 라운드 수를 늘릴 수 있다.
- 라운드 함수 F에 어떤 함수를 사용해도 복호화가 가능
- 암호화와 복호화를 완전히 동일한 구조로 실현할 수 있다.

## 4. 트리플 DES
- 암호화 -> 복호화 -> 암호화로 되어있다.
- 처리속도는 빠르지 않고 안전성도 취약

## 5. AES 선정 과정
- AES(Advanced encryption standard)
- Rijndael = AES
- DES를 대신한 새로운 표준 대칭 암호 알고리즘
- 조건
  - 제한 없이 무료로 이용
  - ANSI C와 Java에 의한 구현
  - 암호해독에 대한 강도의 평가
  - 암호 알고리즘 설계 구격과 프로그램 공개

## 6. Rijndael(라인델)
- 블록길이 :128비트
- 복수의 라운드(round)로 구성(10~14)
  - 128: 10라운드, 192: 12라운드, 256: 14라운드

###### 어떤 암호를 사용해야 하는가?
- DES
  - 사용하지 말것
  - 과거 소프트웨어와의 호환성 유지를 위해 필요
- 트리플 DES
  - 호환성 때문에 앞으로도 당분간 사용
  - 점차 AES로 대체
- AES(Rijndael)
  - 고속, 다양한 플랫폼, 현재까지 안전
  - 사용권장, AES 최종 후로 5개도 사용가능
