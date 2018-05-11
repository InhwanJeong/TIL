Python
=============
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

