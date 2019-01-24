C++언어
===

## 0. 개요

#### 라이브러리
- iostream
- string

#### 이름공간(namespace)
- 식별자(자료형, 함수, 변수 등의 이름)의 영역
- 여러 라이브러리 코드를 포함할때 이름 충돌을 방지

#### c++ 특징
- 객체지향언어
- 상속(inheritance): 클래스를 상속받아 기존 코드를 재사용
- 다형성(polynorphism): 동일한 함수가 객체의 종류에 따라 다르게 동작하는 것
- 연산자 중복(operator overloading): 대상에 따라 동일한 연산자로 새로운 연산을 정의
- 함수 중복(function overloading): 매개변수만 다르면 여러개의 동일한 이름의 함수를 만들 수 있다.
- 캡슐화(encapsulation): 데이터와 함수를 하나의 덩어리(객체)로 묶는것
- 함수 재정의(function overriding): 상속받은 함수를 재정의하여 사용
- new와 delete 연산자: 동적 메모리 할당, 해제
- 제네릭(generics): 클래스 정의를 자료형에 상관없이 재사용하는 기술

```cpp
#include<iostream>

using namespace std;

void main(){

}

```

- auto 자료형
  - 자료형을 자동으로 채워줌
  - 단, 남용하면 좋지않다.

## 1. 입출력

```cpp

cout << "hello world!" << endl;
cout << i << "입니다." << endl;

int k;

cin >> k

```

## 2. 제어구조

```cpp

if(1){

}
else if{

}
else{

}

// switch문
int number

switch (number) {
  case 0:
  case 1:

}


// while 문
while(1){

}


// do-while 문
do{


}while(1);

// for문

for(int i=0; i<10; i++){

}


// 범위기반 for문

int list[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

for(int i : list){
  cout << i << " ";
}

```

## 3. 배열, 함수, 문자열

```cpp

int a[10];
int b[3][5]; // 3: 행, 5: 열

{
  {1, 2, 3, 4, 5},
  {6, 7, 8, 9, 10},
  {11, 12, 13, 14, 15}
};
```

#### 함수
- 값으로 호출(call-by-value)
  - main(값) -> (값)
- 참조로 호출(call-by-reference)
  - main(값) -> (&값)
- 주소로 호출(call-by-address)
  - main(&값) -> (*값)

```cpp

//중복 함수

int square(int i){

}

double square(double i){

}


// 팁

cin >> i;
cin.ignore(); // 엔터키를 없애기 위해 필요

getline(cin, i); // 위 두줄을 이렇게 바꿀 수 있음

```


## 4. 클래스와 객체

#### 클래스
- 접근 지정자
  - private: c++에서 클래스 디폴트 접근지정자
  - public
  - protected

- 멤버 변수(속성, 필드)
- 멤버 함수(메서드)

- 생성자와 소멸자
- getter, setter

```cpp

class car{
private:
  int state; // 멤버변수

public:
  car(); // 생성자
  car(int i);
  car(int a, int b);
  ~car(); // 소멸자

  void go(); // 멤버함수

  int getState() { return state;}// get_state()

  void setState() { this->state = state;} // set_state()


}

```


## 5. 벡터
- 동적 배열

```cpp

vector<int> scores(10);

scores.push_back(10); // 10의 값을 집어 넣는다.

while(scores.empty() != true){
  scores.pop_back();// 가장 늦게들어온 값부터 삭제
}

scores.begin()// 주소값(시작지점)
scores.end()// 마지막값

scores.erase(scores.begin()+ i); // 중간값 삭제


```

## 6. 포인터

```cpp
int num = 10;
int *p
p = &num // p는 주소값, *p는 가리키는 값
p = nullptr // null을 가리킴


// 동적할당

p = new T;
p = new T[N];

int *p;
p = new int[5];

delete p;
delete [] p;


// 객체 동적할당

Dog *pDog = new Dog;

(*pDog).getAge();
pDog->getAge();

const int *p1; // 가리키는 값 변경 x
int * const p2; // 주소값 변경 x
const int * const p3; // 값, 주소 변경 x


```


## 7. 복사생성자 정적멤버
- 복사생성자: 함수끼리 객체를 주고 받을때
- 얕은 복사
  - 원 객체와 복사된 객체가 같은 참조된 데이터를 사용
- 깊은 복사
  - 원 객체와 복사된 객체가 서로 다른 데이터를 사용

```cpp
// 복사생성자 사용법

Myclass(const Myclass& other);


// 복사생성자가 호출되는 경우
Myclass obj(obj2); // 같은 종류의 객체로 초기화

Myclass func(Myclass obj){ // 객체를 함수로 전달

}

Myclass func(Myclass obj){
  Myclass tmp;

  return tmp; // 함수가 객체를 반환하는 경우
}


// 클래스에 깊은 복사 만들기

MyArray(const MyArray& other);

MyArray::MyArray(const MyArray& other){
  this->size = other.size;
  this->data = new int[other.size]; // 새로운 공간 할당
  for(int i = 0; i < size; i++) // 복시
    this->data[i] = other.data[i];
}


// 복사 생성자 vs 대입 연산자

MyArray buffer1(20);
MyArray buffer2(30);
buffer2 = buffer1; // 대입 연산자

MyArray s1;
MyArray s2 = s1; // 복사생성자
MyArray s2(s1); // 복사생성자
MyArray s2{s1}; // 복사생성자

```

#### 정적 변수
- 프로그램 시작과 동시에 생성, 프로그램 종료시 소멸
- 메모리 힙에 저장된다.
- static int count;
  - 모든 객체가 공유한다.


## 8. 상속
- 중복되는 코드 최소화
 ```cpp
 class childclass : public parentclass{

 }


 // 멤버함수 재정의(overriding)

void speak(){
  부모 함수
}


void speak(){
  자식이 재정의
}



// 다중 상속

class sub : public sub1, public sub2{
  // 죽음의 다이아온드
}

 ```

## 9. 다형성과 가상함수
- 다형성
  - 하나의 기호를 여러가지 의미로 사용하는 것



- 상향 형변환
  - 부모클래스 *객체이름 = new 자식클래스();
  - 동적 바인딩(실행중에 호출) virtual

```cpp

virtual void speak(){ cout << "Animal speak()"<< endl;}

void speak() {cout <<"멍멍" << endl;}
void speak() {cout <<"야옹" << endl;}

Animal *a1 = new Dog();
a1 -> speak();

Animal *a2 = new Cat();
a2 -> speak();

```

#### 순수 가상함수
- 순수 가상함수를 하나이상 보유한 클래스 -> 추상클래스
- 객체 생성불가능,
- 선언 O, 정의 x
- virtual void draw() = 0;


## 10. 예외처리와 템플릿
- 예외처리
```cpp

try{
  throw persons
}catch(int e){

}

#### 템플릿
- 함수 템플릿
  - 함수를 찍어내기 위한 틀
  - 자료형의 제한을 없앤다.

```cpp
int get_max(int x, int y){ // double형이 들어올 때 문제 발생
  ~
}

template<typename T>
T get_max(T x, T y){
  ~
}

#define GET_MAX(x,y) ((x)>(y)? (x): (y))

```

- 클래스 템플릿
  - 클래스 내 어디서든 쓸 수있다.
```cpp

template<typename T>
class dog{

}

```

## 11. STL과 람다식
- STL(표준 템플릿 라이브러리)
  - 3가지 컴포넌트(컨테이너, 반복자, 알고리즘)를 제공
  - 시퀀스(sequence)
    - 어떤 순서를 가지고 반드시 시작과 끝이 있다.


#### 컨테이너(자료구조)
  - 배열, 리스트, 벡터, 집합, 사전, 트리, 스택, 큐, MAP 등
  - 아무 자료형이나 저장할 수 있음.
  - 순차 컨테이너
    - 대표적으로 벡터, 리스트
  - 연관 컨테이너
    - 원소들이 key를 가지고 있음
    - 대표적으로 Map(딕셔너리), 집합


#### iterator(반복자)
- 전방향, 양방향, 무작위 방향
- 접근 방식

#### 알고리즘
- 개수(카운팅) 알고리즘
- 탐색 알고리즘
- 비교 알고리즘


#### 람다식
- 함수를 객체로 취급할 수 있는 기능

```cpp
[] (arg1, arg2) 반환형 { body }

auto sum = [](int x, int y) {return x+y;};
cout << sum(1, 2) << endl;



```
