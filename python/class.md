### 정적 메소드(staticmethod)
- 정적메소드를 사용하는 경우
  - self인자를 사용하지 않는 클래스 함수
    
- 정적 메소드의 장점
  - 인스턴스화할 때 static method에 대해서는 bound-method를 생성해줄 필요가 없어 메모리 사용량을 줄일 수 있다.
  - 클래스를 생성하지 않아도 접근할 수 있다.
    
```python
class Test:
    def delete(self, request):
        state = self.__insert_data()
        if state == "fail":
            return False
        return True
    
    @staticmethod
    def __insert_data():
        try:
            pass
        except:
            return "fail"
        return True
```