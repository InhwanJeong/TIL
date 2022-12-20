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