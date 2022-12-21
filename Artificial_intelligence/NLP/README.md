# 자연어 처리(Natural language processing)

## 1. 환경 준비하기
- [아나콘다 설치링크](https://www.anaconda.com/distribution/)
  - 아나콘다 가상환경
  ```bash
  conda create -n {가상환경 이름} # 가상환경 생성
  conda env list # 가상환경 목록 확인
  source activate {가상환경 이름} # 가상환경 접속
  conda deactivate # 가상환경 종료 
  ```
- 프레임 워크 설치
  ```bash
  conda install tensorflow # tensorflow, keras
  pip install gensim # 토픽 모델링과 자연어 처리 오픈 소스 라이브러리
  pip install scikit-learn
  
  pip install nltk # 지연어 처리를 위한 패키지
  import nltk
  nltk.download() # 파이썬 콘솔에서 다운로드
  
  conda install -c conda-forge jpype1 # m1
  pip install konlpy # 한국어 자연어 처리 패키지 
  ```
- m1 jvm error
```bash
# oracle의 JDK 8 설치
# https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html

# ~/.zshrc 환경변수 설정
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk/Contents/Home
export PATH=${PATH}:$JAVA_HOME/bin:
```

## 2. 텍스트 전처리
- 토큰화(Tokenization): 의미 있는 단위로 말뭉치를 나눠주는 것
  - 영어 토큰화
    - 단어 토큰화
    - 문장 토큰화
  - 한국어 토큰화(교착어)
    - 형태소 토큰화
    - 품사 태깅
    - 명사 추출
- 정제(Cleaning)
  - 어간 및 표제어 추출(코퍼스를 줄임)
  - 불용어 제거(잘 안쓰는것, 목적에 맞지 않는 것)
  - 정규표현식을 이용한 제거
- 정규화(Normalization)
  - 정수 인코딩(integer encoding)
  - 패딩(padding)
  - 원-핫 인코딩(one-hot encoding)
    - 정수 인코딩 후 원-핫 벡터로 만들어주는 인코딩
