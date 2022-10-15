# Computer System A Programmer Perspective

## 1. 컴퓨터 시스템 투어
- 컴퓨터 시스템은 하드웨어와 시스템 소프트웨어들로 동작한다.
- hello.c 프로그램의 생명주기에 대해 이해한다.
  - 프로그래머가 프로그램 작성
  - 시스템에서 실행
  - 메시지 출력
  - 프로그램 종료

### 1.1 정보는 Bits와 Context이다.
- 소스코드 프로그램은 비트의 나열, 바이트라고 불리는 뭉치들의 연속으로 이루어져있다.
  - 각 바이트는 문자열을 표시한다.
  - 대부분의 컴퓨터 시스템은 문자를 표시하기 위해 아스키 코드를 사용한다.
  - 텍스트 파일이라고 불리며 이외의 바일들은 이진파일이라고 불린다.
![img.png](resource/ascii_representation.png)

- 시스템의 모든 정보(파일, 메모리, 네트워크로 전송되는 데이터 등)는 비트 뭉치로 이루어져있다.
  - 데이터를 구분하기 위한 유일한 방법 context(문맥, 맥락)이다.
  - 왜냐하면, 연속된 바이트는 정수, 부동소수점, 문자열, 기계명령 등을 나타낼 수 있기 때문이다. 
- 기계는 정수와 실수를 정확하게 표현하지 않는다.
  - 유한한 근사치를 나타낸다.
  - 따라서 예상치 않는 버그가 발생할 수 있다.

### 1.2 프로그램은 다른 프로그램에 의해 번역된다.
- 소스코드 프로그램 인간이 읽을 수 있는 형태의 코드로부터 시작된다.
  - 하지만 프로그램을 실행하면 다른 프로그램으로부터 컴퓨터가 읽을 수 있는 명령 형태로 변환된다.
    - executable object program으로부터 이진파일로 변형된다.
- 유닉스 시스템에서 컴파일러 드라이버(compiler driver)로 소스파일을 오브젝트 파일로 만드는 것은 다음과 같다.
~~~
gcc -o hello hello.c
~~~
![img.png](resource/compilation_system.png)

- 다음 4가지 단계를 거친다.
  - Preprocessing phase. The preprocessor (cpp)
    - 전처리기는 c언어에서 '#'으로 시작하는 부분을 변환한다. 
    - e.g. stdio.h안에 있는 내용을 실제로 가져와서 내용을 채우고 
    - 새로운 c언어 파일 hell.i를 생성한다.
  - Compilation phase. The compiler (cc1) 
    - 컴파일러는 텍스트 파일 hello.i를 어셈블리 언어로 변환한다.
    - 모든 high-level언어는 어셈블리 언어로 변환된다.
    - 어셈블리 언어로 변환된 파일은 hello.s 확장자를 가지게 된다.
  - Assembly phase. Next, the assembler (as) 
    - 어셈블러는 최종적으로 기계가 읽을 수 있는 코드로 변환하게 된다.
    - 변환된 파일을 hello.o(object program)으로 변환된다.
      - 이 이진파일은 메인함수 명령을 실행하기 위해 17바이트를 갖게된다.
      - 이 이진 파일을 텍스트 에디터로 열어볼 경우 알수 없는 문장이 나타나게 된다. 
  - Linking phase
    - hello 파일은 c 라이브러리를 호출하게 되고, printf함수는 printf.o라는 별도의 파일에 존재하게 된다.
    - 이때 두 파일을 합쳐주는 것이 linker이고, 이를 합치게 된 결과가 hello(executable object file)이다.
    - hello 파일은 메모리에 적재되어 실행 가능한 상태로 준비된 파일이다.
- gcc는 GNU에서 만든 유용한 도구중 하나이다.
  - gcc는 다음 언어(C, C++, Fortran, Java, Pascal, Objective-C, and Ada)를 번역할 수 있다.
  - GNU는 gcc외 다른 프로그램(emacs editor, gcc compiler, gdb debugger, assembler, linker, utilitie)을 개발했다.