## 공개키 방식
- RSA

## 암호화와 복호화
- 평문(plaintext): 암호화하기 전의 메시지
- 암호문(ciphertext): 암호화한 후의 메시지
- 암호기술: 중간에 도청자가 암호문을 가로채도 복호화 할 수 없다면 내용을 알 수 없는 기술

암호화 <---> 복호화

해독: 불법적으로 암호를 풀어 내는 행위


- 평문 + 키 (암호화) --> 암호문
- 암호문 + 키 (복호화) --> 평문
- 암호는 기밀성을 보장

- 암호해독 : 수신자 이외의 사람이 암호문으로부터 평문을 복원하려고 시도하는 것
- 암호화 알고리즘 : 공개되어 있음, key의 비밀유지가 중요
  - KEY의 경우의 수가 너무 많기 때문에 알고리즘이 공개되어 있어도 안전하다.

## 암호 시스템의 요소
- 평문, 암호문, 암호화(복호화)알고리즘, 키
- 기호적 표현
  - P(평문), K(키), E(암호화), C(암호문), D(복호화)


## 대칭 암호와 비대칭 암호
- 대칭 암호: 암호화 키 == 복호화 키   (빠름)
- 비대칭 암호: 암호화 키 != 복호화 키
  - 키쌍(pair): 공개키 + 개인키
  - 공개 키 알고리즘이라고도 한다
  - 공개키(PKI, public key infra)

#### 하이브리드 암호
  - 대칭키 공개키 장점을 합침

#### 일방향 해시 함수(one-way hash function)
  - P -> hash -> 해시 값
  - 기밀성 x, 무결성을 점검
  - 평문, 역으로 되돌리는 것이 불가능

#### 메시지 인증 코드

#### 디지털 서명
- 공개키 공인인증서

#### 의사난수 생성기
- 난수열을 생성하는 알고리즘

## 보안 위협과 암호 기술에 의한 방지

| 보안 위협 | 위협받는 특성     | 방지를 위한 암호 기술|
| :------------- | :------------- | --- |
| 도청     | 기밀성       |  암호화 |
| 메시지 변경| 무결성       | 일방향 해시 함수 |
| 위장     |   인증      | 메시지 인증 코드 |
| 부인     |  부인 봉쇄   | 디지털 서명 |

## 스테가노그래피와 디지털 워터마킹
- 크립토그래피(cryptography)
  - 메시지의 내용을 읽지 못하게 하는 기법
- 스테가노그래피(steganography)
  - 메시지의 내용을 읽지 못하는게 아니라 메시지 존재 자체를 숨기는 기법

- 디지털 워터마킹
  - 파일 중에 저작권자나 구입자의 정보를 집어넣는 기술
  - 일반적으로 디지털 워터마킹 기술에 스테가노그래피 기술을 적용

## 암호와 보안 상식
- 비밀 암호 알고리즘을 사용하지 말 것
  - 비밀 암호 알고리즘을 사용하는 것이 아닌 공개 되어 있는 강한 암호 알고리즘을 사용해야한다.
  - 암호 알고리즘의 비밀은 반드시 폭로 된다.
- 약한 암호는 암호화 하지 않는 것보다 위험
  - 사용자는 암호의 강도와 상관없이 암호화가 되어있다는 사실만으로 안심 -> 취약점
- 어떤 암호라도 언젠가는 해독된다.
- 암호는 보안의 아주 작은 부분이다.