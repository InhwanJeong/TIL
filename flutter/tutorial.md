# flutter 튜토리얼

#### statelesswidget 스캐폴드
- stless 자동완성을 이용하면 다음과 같이 statelesswidget 기반의 스캐폴드가 완성됨.
- MaterialApp은 구글기반의 템플릿과 
~~~
class  extends StatelessWidget {
  const ({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp();
  }
}
~~~

#### 기초 위젯

~~~
class  extends StatelessWidget {
  const ({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container();
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

### Align 위젯

### Row 위젯
- 여러 위젯을 가로로 배치하는 위젯

### column 위젯
- 여러 위젯을 세로로 배치하는 위젯


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
