## 디지털 신호

```
빛, 소리, 신호
  -> 아날로그
    -> 디지털
      -> 저장 및 가공
        -> 아날로그
          -> 사운드, 이미지 , 비디오
```

- 프랑스 수학자 푸리에(Fourier)
  - 어떠한 불규칙한 모양의 파형도 정현파의 합으로 표현될 수 있다.
  - 정현파: sin 또는 cos곡선과 같은 파장과 진폭이 일정한 파형

#### 디지털 신호를 사용하는 이유
- 컴퓨터를 통한 다양한 신호 처리 가능
  - 컴퓨터에 신호가 숫자로 입력되면 컴퓨터는 더 이상 신호로 보지 않고 숫자로 보아 여러 가지 일을 수행
  - 이러한 점이 신호를 디지털화하는 가장 큰 이유

- 정확성 보장
  - 데이터가 외부환경의 변화에 영향을 받지 않고 정확한 데이터로 조작이 가능

- 완전한 재생 기능
  - 아날로그에 비해 똑같은 연산을 항상 같은 성능에서 재생이 가능
  - 녹음이나 복사 등이 자유자재로 이루어짐

#### 신호의 디지털화
- 표본화(Sampling)
  - 나이퀴스트(Nyquist) 표본화 정리
  - 앨리어스 신호(Aliased Signl)
- 양자화(Quantization)
- 부호화(Encoding)

###### 기본개념
- 일정한 시간 간격마다 아날로그 신호의 크기를 숫자로 나타낸 것
  - 표본화: 신호를 일정한 간격으로 잘라 이산신호 만들기
  - 양자화: 각 표본 신호의 크기를 계량화 하는 단계
  - 코드화: 표본 값을 컴퓨터에 나타내기 위해 부호화

#### 표본화
- 표본화는 X축에 해당되는 값을 결정
- 양자화는 Y에 대한 눈금을 구하는 것
- 파동의 크기를 나타내기 위해 일정한 간격으로 X축에 눈금을 정하는 것
- X축은 시간축이기 때문에 표본화는 초당 몇 번할 것인가를 정하는 것을 표본화율라 함

###### 나이퀴스트 표본화 정리
- 최적화된 표본화
- 신호를 주파수 영역으로 표현했을 때 가장 빠른 주파수 성분을 fmax라고 하면 신호내에 있는 유효한 정보를 디지털로 모두 표현하기 위해서 적어도 fmax의 2배 이상으로 표본화해야 한다. 즉 가장 빠른 주파수의 2배로 표본화하면 된다.
  - 전화 음성신호의 최대 주파수 성분은 4KHz이기 떄문에 8KHz이상으로 표본화 해야한다.

###### 앨리어스 신호
- 최대 주파수보다 적게 표본화하게 되면 원래 신호와 다른 신호로 만들어진다. 이를 앨리어스 신호라고 한다.

#### 양자화
- Y축의 눈금을 정하는 과정이 양자화라고 함
- 양자화 오류: 정화하게 일치된 Y축의 값이 없으면 가장 가까운 값으로 대응 되게 되는데 이를 양자화 오류라고 한다.
- 눈금자 결정
  - 신호 범위를 넓게: 오류 증가, 용량 감소
  - 신호 범위를 세밀하게: 오류 감소, 용량 증가

#### 부호화
- 저장공간을 줄이고 가공을 좀더 쉽게 하기 위해 코드화하는 단계
- Y축의 값을 그대로 저장하기 보다는 2진수로 부호화 하여 저장 공간을 줄임
  - 2진수로 부호화하는 데 필요한 비트 수는 Y축의 눈금의 개수에 달림

## 아날로그 신호 재생
- 디지털 데이터의 아날로그 변환 -> 평탄화 과정
- 디지털 데이터는 아날로그로 표현하면 계단 모양이 됨
- 양자화 오류 때무네 필수적으로 생길 수밖에 없는데 원래의 신호와 많이 다름
- 원래 신호에 가깝도록 계단 모양을 평탄하게 해줌