## Dart
- google에서 개발한 언어이며, 자바스크립트를 대체 하고자 개발 되었지만, 자바스크립트를 대체 하지는 못함.
- flutter라는 크로스 플랫폼 개발 도구에서 사용되는 언어
- c++, java와 많이 유사함.
- Dart는 변수를 사용할 때 camel case를 사용하도록 한다.
  - e.g. is_good(x) -> isGood(O)

### hello world
- 세미콜론을 반드시 붙여 주어야 함.
- 함수에는 리턴형을 항상 명시 해줘야 함.
  - main()함수는 항상 void로 리턴해야 함.
~~~dart
void main(){
    print("hello world");
}
~~~
- 함수를 사용한 hello world
~~~dart
void main(){
    hello("world");
}

void hello(String message){
    // 출력문에서 $를 이용하여 간단하게 사용가능
    print("hello $message");
}
~~~

### import 문
- Dart-SDK는 다양한 라이브러리를 제공
  - dart:core 라이브러리만 자동으로 로드
  - dart:html, dart:async, dart:mach 등 다양한 라이브러리를 사용하기 위해서는 직접 로드
- 
~~~Dart
import 'dart:io';
~~~

### 주석
~~~Dart
// 한줄 주석

/*
    여러줄 주석
*/
~~~


### 변수
- 변수는 항상 형식을 지정 해야 함. 
~~~Dart
// 기본 자료형
String message = "inan";
int count = 1;
double pi = 3.14;
bool is_good = true; // true, false (소문자로 값 대입)

// dart 고유 자료형
num length = 2.3; // int와 double의 supertype
var item = 2; // 초기에 설정된 자료형으로 쭉 사용(데이터 변경 시 자료형 변경 되어선 안됨.)
dynamic item2 = "test"; // 모든 자료형 항상 변환 가능

// collection
List<String> names = []; //문자열 리스트
List<int> ages = []; //정수 리스트
Map<String, int> people = {"a":1};//문자열 키와 정수 값을 갖는 맵
Set<String> names2 = {"inan", 'inan', 'inana'}; // 순서가 없고 중복이 없는 collection

// 상수
int get(){
    return 10;
}
const PRICE = 1.43; // 컴파일 시점에 상수가 됨.
final MYNAME = "inan";

const value = get() // ERROR! 
final value = get() // OK
~~~