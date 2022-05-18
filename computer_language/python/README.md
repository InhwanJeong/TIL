# python

## 핵심
1. 파이썬의 버전을 알아두자.
2. PEP8 코딩 가이드를 준수하자.
3. 가상환경을 반드시 사용하자.
4. 

## 일급 함수, 일급 객체, 클로저
- 일급 객체란 아래 3가지 조건을 충곡하는 객체를 일급 객체라고 부른다.
    - 변수에 할당 할 수있어야 한다.
        - book_object = Book() 
    - 객체의 인자로 넘길 수 있어야 한다.
        - manage_book(book_object, index)
    - 객체의 반환값으로 객체를 반환할 수 있야하 한다.
        - return book_object

- 일급 함수란, 함수를 다른 변수와 동일하게 다루는 언어는 일급함수를 가졌다고 한다.
    - javascript와 python, go, kotlin의 함수는 일급함수이다.
    
- 클로저
    - 변수의 값은 누군가에 의해 언제든지 변경될 수 있어 오류 발생의 근본적 원인이 될 수 있다. 상태 변경이나 가변(mutable) 데이터를 피하고 불변성(Immutability)을 지향하는 함수형 프로그래밍에서 부수 효과(Side effect)를 최대한 억제하여 오류를 피하고 프로그램의 안정성을 높이기 위해 클로저는 적극적으로 사용된다.
    
## 제너레이터
- 제너레이터는 모든 값을 포함한 배열 또는 리스트를 만들어서 리턴하는 대신에 yield 구문을 이용하여 한번 호출에 하나의 값만 리턴한다.
  - 모두 사용 후 가지고 있던 모든것이 메모리에서 사라진다.
- 제너레이터는 메모리를 절약해야하는 상황에 사용해야한다!
    - 속도가 중요할때는 리스트에 담아서 속도를 향상 시켜야 함.
    
```python
def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1, 2, 3, 4, 5])  #1

print(my_nums)
>> <generator object square_numbers at 0x0000016B17E19EB0>

def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

>> 1
4
9
16
25

print(next(my_nums))

>>Traceback (most recent call last):
 StopIteration

 # 제너레이터
my_nums = (x*x for x in [1, 2, 3, 4, 5])  #1
```

```python
import datetime


class DatetimeDecorator:
        def __init__(self, f):
                self.func = f

        def __call__(self, *args, **kwargs):
                print(datetime.datetime.now())
                self.func(*args, **kwargs)
                print(datetime.datetime.now())



class MainClass:
        @DatetimeDecorator
        def main_function_1():
                print("MAIN FUNCTION 1 START")



        @DatetimeDecorator
        def main_function_2():
            print("MAIN FUNCTION 2 START")



        @DatetimeDecorator
        def main_function_3():
                print("MAIN FUNCTION 3 START")




if __name__ == '__main__':    
    my = MainClass()
    
    my.main_function_1()    
    my.main_function_2()    
    my.main_function_3()

```