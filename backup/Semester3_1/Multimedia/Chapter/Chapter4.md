## 데이터 압축

#### 압축의 필요성
- 대용량 멀티미디어 데이터를 컴퓨터에 저장하거나 네트워크를 통해 다른 기기에 전송하는데 많은 자원이 소모
- 데이터 크기를 줄여 저장공간과 저장 대역폭을 효율적으로 이용하기 위해 압축이 필수적이다.

#### 데이터 중복성
- 데이터의 중복성이 존재하기 때문에 부호화를 통하여 데이터의 압축가능
- 데이터의 중복성이란 하나의 데이터에 동일하거나 비슷한 정보들이 반복되어 나타나는 것을 의미
  - 시간적 중복성: 시간의 흐름에 따라 같은 정보가 반복됨
  - 공간적 중복성: 같은 정보가 다른 공간적인 위치에 반복됨
  - 통계적 중복성: 자주발생하거나 드물게 발생하는가 확인
  - 스펙트럼 중복성: RGB 밝기가 중요한가 또는 색감이 중요한가 확인

#### 압축 시스템의 평가
- 압축율: 압축 이전의 데이터 크기와 부호화 과정을 거친 압축된 데이터 크기의 비율로 정의
- 복원된 데이터의 품질
  - 문서 데이터는 복원된 데이터 정보가 명확해야 함으로 손실이 없이 복원할 수 있는 방법인 무손실 압축을 채택
  - 소리나 영상데이터는 복원된 데이터와 압축되기 이전 데이터가 동일 하지않더라도 큰 문제가 없음 -> 손실 압축
- 압축/복원 속도
  - 응용에 따라 데이터의 압축속도는 중요하지 않은 기준이 될 수 있음
  - 대화형 멀티미디어 응용에서는 데이터의 압축속도가 중요한 평가 기준이 됨

#### 압축 기법의 종류
- 무손실 압축(lossless compression)
  - 연속길이 부호
  - 렘펠-지브-웰치(LZW) 부호
  - 허프만 부호
  - 산술 부호
- 손실 압축(lossy compression)
  - 변환기법: FFT, DCT
  - 예측기법: DPCM, ADPCM, DM, ADPCM
  - 양자화
  - 보간 기법
- 혼성 압축(hybrid compression)
  - JPEG, MPEG, H.261...