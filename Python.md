Python
=============

PyPI(Python Package Index) : 파이썬 모듈을 제공하는 중앙 리포지토리

# 0.주석
한줄 주석 : #   c언어 //    
여러줄 주석 : '''   ~   '''   c언어 /*   ~     */    

# 1.출력 & 입력    
print("Hello World!")   
num = input("값을 입력하세요: ")

# 2.변수 & 연산자
선언&초기화    
x = 1   
a ,b = 3, 4   
num = 10.0    
name = 'hello' or name = "hello"    
name = "Jeong In Hwan"    
연산자는 c랑 동일하며 거듭제곱 연산자인 **가 있다.  ex) 2**10 -> 2의 10승

# 3.리스트
mylist = []   // mylist = [1,2,3]   
mylist.append(1)    
mylist.append(2)    
mylist.append(3)    

print(mylist[0])    
print(mylist[1])    
print(mylist[2])    

for x in mylist:    
    print(x)
    
# 4.포맷스트링
```python
name = "John"   
age = 23    
print("%s is %d years old" % (name, age))   
```
# 5.조건문
if 조건 ==조건:   
elif 조건 < 조건:   
else:   

# 6.반복문   
### while문
while 조건문   
else    

### for문
for 변수 in range(초기화값, 반복횟수, 증가값):     
// for(int i=0;i<8;i++)  == for i in range(0, 8, 1)   "0~7 출력"    
for i int range(1, 5):     //   1~4출력     

# 7.함수
### def 함수명   

def Say_hello():    
    print 'hello'   

호출 : Say_hello()    

### 매개변수 & 디폴트: def sum(a, b = 10):   

### varargs 매개 변수
임의의(variable) 개수의 매개변수(인수(arguments))   
ex) 
```python
def total(initial = 5, *numbers, **keywords):   
  count = initial   
  for number in numbers:    
    count += number   
  for key in keywords:
    count += keywords[key]
  return count
print total(10, 1, 2 ,3, vegetables = 50, fruits = 100)
```
-------------
결과: 166
-------------

### 8.모듈

모듈을 불러오기 위해서 import를 사용
```
import 모듈  -> 모듈 전체
from 모듈 import (변수/함수) -> 모듈의 일부분
del 모듈 -> 모듈을 제거
```
##### 대표적인 모듈
- sys : 파이썬 인터프리터 제어 #ex) sys.ps1(현재 프롬프트), sys.exit()
- os : 운영체제를 제어
- string : 기본적인 문자열 연산 제공
- re(regular expression) : 문자열 정규 표현식
- webbrowser : 웹브라우저 관련 모듈
- random : 난수 관련 모듈

##### 모듈 배포, 다운로드
- 배포 : python3 name.py sdist
- 다운로드 : sudo python3 name.py install

```
파이썬 모듈은 네임스페이스를 만든다
-> print_name()      -> (x) # 만약 from name import print_name로 했다면 이 문법이 옳다
-> name.print_name() -> (O) # imporn name
```

### 9. 리스트
```
Name = ["Jim", "Minho" , "Inan"]
```
- 변수 앞에는 데이터타입 형을 지정하지 않는다.
- len(list) : 리스트안의 항목 개수 출력 
- append("") : 리스트 맨 뒤 항목 추가
- pop() : 리스트 맨 뒤 항목 반환(삭제)
- extend(["",""]) : 여러 항목 추가
- remove(" ") : 특정 항목 제거
- insert(위치, "" ) : 위치 앞에 항목 추가

```python
Name = ["Jim", "Minho" , "Inan"]

for each_flick in Name:   # for 타깃 식별자 in 리스트: 
    print(each_flick)
```

##### 결과

```
Jim
Minho
Inan
```

##### isinstance(A,B) : A가 B가 맞는지 확인하고 반환
```python
names = ['Michael', 'Terry']
isinstance(names, list) # names가 list인가?
#True
num_names = len(names)
isinstance(num_names, list) #num_names가 list인가?
#False
```

### 내장 함수
- 파이썬에 모듈을 추가하지 않고 쓸 수 있는 기본함수
- 프로그래밍 업무를 간단하게 하기 위해 존재       
1.range() : 필요에 따라 주어진 범위의 일련의 숫자를 생성하는 나열자를 반환     
for num in range(4) -> 배열의 0~3까지       
2.abs() : 어떤 숫자를 입력 받았을때, 그 숫자를 절대값으로 돌려주는 함수       
abs(-3) -> 3  abs(3)  -> 3      
3.all() : 받는 인수가 모두 참이면 true, 거짓이 하나라도 있으면 false        
4.any() : 받는 인수가 하나라도 참이면 true, 모두 거짓이면 false       
5.chr() : 숫자 인수 -> 아스키코드 변환해주는 함수       
5-1.ord() : chr() 반대        
6.enumerate : 리스트를 생성하며 인덱스번호와 함께 반환        
7.id() : 객체를 입력받아 객체의 고유 주소값을 반환하는 함        
8.isinstance(object, class) : 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 true 거짓이면 false 반환       
9.len() : 입력값의 길이를 리턴하는 함수      
10 int() : 입력값을 무조건 정수형으로 반환하는 함수       
11.list() : 리스트를 반들어서 반환하는 함수       
12.max() : 반복가능한 자료형을 입력받아 최대값을 반환하는 함수     
13.min() : " 최소값을 반환하는 함수       
14.sorted() : 입력값을 정렬한 후 반환하는 함수        
15.round() : 입력값을 반올림하여 반환하는 함수     
16.pow(x,y) : x를 y번 곱하여 반환 -> x의 y제곱        
17.open(filename,"mode") : w : 쓰기모드 r : 읽기모드 a: 추가모드 b: 바이너리 모드




