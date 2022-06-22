# flutter 튜토리얼

#### statelesswidget 스캐폴드
- stless 자동완성을 이용하면 다음과 같이 statelesswidget 기반의 스캐폴드가 완성됨.
- MaterialApp은 구글기반의 Material 디자인과 기능을 사용할 수 있는 class이다.
  - 개발에 많은 것을 줄여준다.
~~~
class  extends StatelessWidget {
  const ({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp();
  }
}
~~~

### scaffold 위젯
- 상, 중, 하단의 레이아웃을 가지는 위젯
~~~
Scaffold(
    appBar: AppBar(),
    body: Container(),
    bottomNavigationBar: BottomAppBar(),
)
~~~

### container 위젯
- 컨테이너 위젯은 직사각형의 시각요소 위젯이다.
- BoxDecoration클래스를 통해 배경, 보더, 그림자 등을 설정할 수 있다.
-  margins, padding, size등을 줄 수 있다.

### Align 위젯

### Row 위젯
- 여러 위젯을 flex하게 가로로 배치하는 위젯

### column 위젯
- 여러 위젯을 flex하게 세로로 배치하는 위젯

### stack 위젯
- 웹의 absolute positioning layout model을 기반으로 한다.

### Text 위젯
- 텍스트를 추가하기 위한 위젯
- style: TextStyle
  - fontSize: 폰트 크기 조절
  - fontWeight: 폰트 굵기
  - color: 색상 지정
~~~
Text("텍스트 기본위젯")
Text("텍스트 기본위젯",
    style: TextStyle()
)
~~~

#### (1) 색상 넣기
1. Colors.색상
2. Color(0xff1D438A)
3. Color.fromRGBO(209, 239, 237, 1)

### button 위젯
- 버튼 종류
  - TextButton
  - ElevatedButton
  - IconButton
- 필수 위젯
  - child
  - onPressed

### image 위젯
