## 디지털 이미지
- 시각적 정보, 인간이 받아들이는 정보 중 시각적 정보는 전체 정보 중 상당 부분
- 멀티미디어 디자인에서 가장 중심적인 위치
- 이미지
  - 스캐너, 디지털 카메라와 같은 입력 장치를 이용하여 생성된 그림
- 그래픽
  - 일러스터와 같은 컴퓨터 소프트웨어를 통하여 생성된 그림

#### 화소
- 회소(pixel)
  - picture Element(화면 요소)의 합성어
  - 화면을 구성하는 가장 기본단위
  - 이미지는 화소의 집합으로 표현, 비트맵(bitmap) 방식으로 저장
- 색상의 수
  - 각 화소는 RGB의 값을 적정히 배합시켜 색을 표현
  - 색상의 수는 화소당 비트에 비례: 2의 n승개 색상
    - 즉, 할당된 비트수가 클수록 더 많은 컬러 가능

- 비트수와 색상
  - 1비트: 흑백
  - 4비트: 팔레트 사용(인덱스 컬러)
  - 8비트: 팔레트 사용(인덱스 컬러)
  - 16비트: 하이컬러(R:G:B = 5:5:5)
  - 24비트: 트루컬러(R:G:B = 8:8:8)
  - 32비트: 트루컬러 + 알파채널

#### 해상도
- 장치 해상도(Device resolution)
  - 단위 길이당 표시할 수 있는 화소 또는 점의 수로 표현
  - 인치를 단위 길이로 많이 사용, 이 경우 해상도의 단위는 dpi(dot per inch)
  - 프린터, 스캐너: 300 ~ 700dpi이상, 모니터: 85 ~ 120 dpi이상

- 이미지 해상도(Image resolution)
  - 장치와 무관한 이미지 자체의 해상도
  - 전체 화소의 수(또는 가로 세로 화소 수)로 표현
  - 디스플레이, 카메라, 이미지 등의 해상도에 적용

#### 이미지와 래스터/벡터 그래픽

###### 래스터 그래픽
- 화소단위로 저장하는 방식-> 이미지, 정지영상
- 화면을 확대할 때 화질이 떨어진다: 계단현상-> 앨리어싱
- 파일의 크기는 해상도에 비례
- 칠하기 도구, 사진편집도구에서 사용하는 방식

###### 벡터 그래픽
- 점, 선, 곡선, 원등의 기하적 객체(즉, 그래픽함수)로 표현되므로, 화면 확대시 화질의 변화가 없다
- 일반적으로 파일의 크기가 래스터 그래픽 방식에 비해 작다.
- 그리기 도구에서 점/선/원/다각형 등 기하 객체 생성

<br>
<br>

## 컬러 모델
- 빛의 특성
  - 진폭: 빛의 밝기를 결정
  - 파장: 빛의 색상 결적

#### RGB 모델
- 빛의 삼원색이 기본이 되는 컬러 모델
- 여러색을 더하면 흰색이 되는 빛의 성질을 이용
- 기본색을 더하여 새로운 컬러를 만들어 내므로 가산 모델이라고 불린다.

#### CMY 모델
- 감산모델이라고 불리며 CMY(Cyan, Magenta, Yellow)를 사용
- 빛의 혼합에 의해 발생한 2차 색상들을 기본으로 하는 컬러 모델
- 물감, 잉크 등의 성질을 이용하는 컬러프린터나 인쇄등에 사용
- CMYK 모델을 많이 사용, K(Kappa) 검은색
  - CMY를 섞으면 검은색이 생성되지만 만족스럽지 못하며 잉크 낭비

#### HSV(Hue, Saturation, Value) 모델
- 인간의 시각 모델과 가장 흡사한 컬러모델, 인간의 직관적인 시각에 기초를 둠
- 색상, 채도, 명도의 세가지 속성 이용

<br>
<br>
