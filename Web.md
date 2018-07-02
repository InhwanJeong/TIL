Web Programming
==============================

## 0.개요

- 기획 -> 디자인 = 개발 -> 테스트

#### 서버와 클라이언트
###### 서버

서버 | 계층
--- | ---
WebServer(아파치, IIS, Nginx) | 3층
미들 웨어(PHP, python, Java) | 2층
데이터 베이스(MySQL, Oracle) | 1층

```
아파치 + (PHP, Python, Java) + (MySQL, Oracle)
         -서버의 프레임(뼈대)-
```

###### 클라이언트
- 웹브라우저(web client): Chrome, IE, Firefox...


##### localhost 
- 내 컴퓨터 자체에 설치 되어있는 웹 서버에 접속해서 요청한다.
```
local/index.html  // 내 컴퓨터 웹서버에 있는 index.html 파일 요청
```

## 1. 서버 설치
- bitnami lamp(리눅스,아파치,mysql,php) : 서버의 뼈대를 모두 한번에 다운로드 받을 수 있다. 
```
https://bitnami.com/stack/lamp
$ chmod 755 bitnami...
$ sudo ./bitnami...
```

#### apache2/htdocs
- 클라이언트가 요청했을때 파일을 찾는 최상위 루트 디렉터리

#### 서버 프로그램 실행&제어
- 첫번째 방법
```
$ cd /opt/lampstack-7.1.19-0
$ sudo ./manger-linux-x64.run
```
- 두번째 방법(별명)
```
*별명작성*
$ alias bitnami='cd /opt/lampstack-7.1.19-0;sudo ./manger-linux-x64.run'
그 이후
$ bitnami
```

## 2.HTML(Hyper Text Markup Language)
- HyperText: 문서가 서로 연결 되어있는 개념(링크)
- Markup language : 태그(Tag)-> 부가설명
- 시작태그 <>  컨텐츠  끝태그 </>
- Tag reference

#### head 태그
- 문서를 설명하는 정보를 감싸는 태그
- <meta charset="utf-8" /> : 문서가 utf-8로 되있다는것을 알려줌, 이것이 없으면 한글이 깨지니 가급적 사용
- title 태그 : 웹 브라우저의 이름을 바꾼다(디폴트는 파일이름) 
- <!DOCTYPE html> : HTML 5의 타입을 써서 만들었다는 것을 알려줌, 그 외에도 굉장히 많다.

#### body 태그
- 본문을 나타내는 태그

#### a 태그
- <a> 링크 </a>
- 속성(href) : 링크를 눌렀을 때 이동할 주소
- 속성(target="_blank") : 링크를 눌렀을 때 새 창으로 주소를 이동
```
<a href="http://github.com/InhwanJeong" target="_blank">Hello</a>
```

#### li 태그
- 리스트 태그(강조)
- ul(unordered list) 태그 : 구분, 묶어주는 태그
- ol(ordered list) 태그 : 순서를 붙여주는 태그
```
<ul>
<li> inan1 </li>
<li> inan2 </li>
</ul>

<ul>
<li> inan3 </li>
<li> inan4 </li>
</ul>
```





## PHP(Hypertext Preprocessor

- 프로그래밍 언어의 일종으로 동적 웹 페이지를 만들기 위해 설계되었음
- 대표 PHP 기반 BBS : 제로보드, 텍스트큐브, 그누보드, XpressEngine 
- c언어 스타일을 따른다.
- 서버 사이드 스크립트
