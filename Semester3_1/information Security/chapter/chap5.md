## 1. 블록 암호 모드
- 블록 암호
  - 어느 특정 비트 수의 집합을 한번에 처리하는 알고리즘

- 스트림 암호
  - 데이터의 흐름을 순차적으로 처리해가는 알고리즘
  - 1비트, 8비트, 혹은 32비트 등의 단위로 암호화 복호화

- 암호 모드
  - ECB 모드
  - CBC 모드
  - CFB 모드
  - OFB 모드
  - CTR 모드

## 2. ECB(Electric codeBook)모드
- 평문 블록을 암호화한 것이 그대로 암호문 블록
- 패딩(padding)
  - 마지막 평문 블록이 블록 길이에 미치지 못할 경우에 추가하여 블록 길이가 되도록 맞춘다.
  - 안전하지 않다. 사용 X

#### ECB모드의 특징
- 가장 기밀성이 낮은 모드
- 암호문을 살펴보는 것만으로도 평문 속의 패턴 감지
- 1:1 대칭 암호

## CBC(Cipher Block Chaining) 모드
- 암호 블록 연쇄 모드
- 많은 곳에서 사용 중(권장)

## CFB 모드
- 현재는 사용안함 CTR을 사용하는게 나음

## OFB 모드

## CTR(counTeR) 모드
- CTR모드는 1씩 증가해가는 카운터를 암호화해서 키 스트림을 만들어내는 암호
- 병렬 처리가 가능하며 간단하다.

#### CTR 모드의 특징
- 암호화와 복호화가 완전히 같은 구조
- 구조가 매우 단순하다.(권장)
-

#### OFB 모드 vs CTR 모드
- CTR
