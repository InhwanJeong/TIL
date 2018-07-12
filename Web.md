Web Programming
==============================

Web IDE : Atom(아톰) + emmet(아톰 내부에서 설치)
-------------
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


## css(Cascading Style Sheets)
- HTML과 함께 쓰인다. (HTML을 꾸며주기 위해 만들어진 언어)
- 문법 : 선택자(selector) + 서술(description)
- 예(HTML의 style 태그안에 들어간다)
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style media="screen">
          h1{color:red; font-size: 100px}
          h2{text-decoration: underline;}
          header h1{border: 10px solid red;}
          #selected{
        border: 1px red solid;
      }
    </style>
    <title>이난's 홈페이지</title>
  </head>
  <body>
  <header>
    <h1>CSS</h1>
  </header>
    <h1>PHP</h1>
    <h2 id = "selected">JavaSscripts</h2>
    <h3>HTML</h3>
  </body>
</html>
```

#### 박스 모델
- margin : 
- border :
- padding : 
- width, height :
## PHP(Hypertext Preprocessor

- 프로그래밍 언어의 일종으로 동적 웹 페이지를 만들기 위해 설계되었음
- 대표 PHP 기반 BBS : 제로보드, 텍스트큐브, 그누보드, XpressEngine 
- c언어 스타일을 따른다.
- 서버 사이드 스크립트

## HTTP(HyperText Transfer Protocol)
- 팀 버너스 리가 웹을 만들면서 개발한 프로토콜로 현재 가장 많이 쓰임
- 텍스트, 그래픽, 애니메이션을 화면에 보여주고 사운드를 재생해준다.
- HTTP를 이용하여 서버에 연결하기
```
1.connect                  #클라이언트
2.Request(.html)           #클라이언트
3.Response(.html)          #서버
```
- 메서드( GET, HEAD, POST, PUT, OPTIONS, DELETE, TRACE, CONNECT )
- HTTP 프로토콜은 데이터가 네트워크 장비를 통과할때 암호화되지 않은 단순한 TCP를 사용하기 때문에 공격자가 정보를 가로챌 수 있다.

#### HTTPS(HTTP over Secure Socket Layer)
- 애플리케이션 계층 프로토콜으로 HTTP에서 보안이 강화된 버전
- SSL(Secure Socket Layer)을 이용하여 클라이언트와 서버 사이에 주고받는 정보를 보호하는데 사용된다.

### 1. Request 패킷
- Request 패킷으로 GET, POST, HEAD와 같은 메서드가 있다.

#### GET 메서드
- 일반게시판, 목록등 접근 자유도를 부여하기 위해 GET방식 사용
```
GET / HTTP/1.1

Accept : text/html, application/xhtml+xml, */*
Accept-Encoding: gzip, deflate

Cookie: HSID=AaxlkkovV2snlEi6UQ; SSID=AAYVu_evC0Tiu3aVc;
APISID=JEWp0eojRTLFtYKJ/ACgEWj_0mL8Li_-fl;
SAPISID=kabRBO-uT0ebDcfc/A2byDX--FwN649tHw

Host: www.google.comConnection: Keep-Alive
Accept-Language: ko-KR
User-Agent: Mozilla/5.0 (compatible; MSIE9.0; Windows NT6.1; Trident/5.0)
```
- 첫번째 줄 : HTTP전송방법(GET을 많이 사용) / 요청된 URL / HTTP 버전
- Cookie, HSID, SSID, APISID, SAPISID : 서버가 클라이언트에 전송한 인자값에 추가 정보를 보낼 때 사용
- Host : URL 주소에 나타난 호스트명을 자세하게 나타내기 위함
- User-Agent :  브라우저나 기타 클라이언트의 소프트웨어 정보를 표시

#### POST 메서드
- URL을 통해 인수값을 전송하지 않음 -> 안전한 편
- 글을 저장, 수정, 삭제하는 작업을 할때 보안을 위해 POST방식을 사용
```
POST / HTTP/ 1.0
Accept: */*X-CI : 126323033
X-AT: OVERNET
X-GO: 1;KR;842;9530
X-DM: www.google.co.kr
X-SP: 762
Host: dr1.webhancer.com
Content-Length: .
Pragma : no-cache
Connection: Close
```

#### 기타 메서드
- HEAD : 서버 쪽 데이터를 검색하고 요청하는데 사용된다.
- OPTIONS : 자원에 대한 요구-응답 관계에서 관련된 선택사항에 대한 정보를 요청할때 사용, 이를 통해 클라이언트는 어느 것을 선택할지 결정 할 수 있으며, 자원과 관련된 필요사항도 결정하고 서버의 수행능력에 대해서도 알아볼 수 있다.
- PUT : 메시지에 포함되어있는 데이터를 지정한 URI(uniform resource identifier)장소에 지정된 이름으로 저장한다.
- DELETE : URI에 지정되있는 자원을 서버에서 지울 수 있게 한다.
- TRACE : 요구 메시지의 최종 수신처까지 루프백 검사용으로 사용. 즉 클라이언트~(프록시, 게이트웨이)~서버에 이르는 경로를 알아냄

### 2. Response 패킷
- 서버에서 쓰이는 프로토콜 버전, 상태 코드, 전달할 데이터형식, 데이터 길이 등과 같은 추가 정보가 포함되어있다.
- 데이터 전달 완료시 서버는 연결을 끊는다.

상태코드 | 함축적 의미 | 설명
---   | --- | ---
100번대 | 정보 전송 | 임시 응답을 나타내는 것은 Status-Line과 선택적인 헤더로 이루어져 있고 빈줄로 끝을 맺는다.
200번대 | 성공 | 클라이언트의 요청이 성공적으로 수신되어 처리 되었음을 의미한다
300번대 | 리다이렉션 | 클라이언트의 요구 사항을 처리하려면 다른 곳에 있는 자원이 필요하다는 것을 의미
400번대 | 클라이언트 측 에러 | 클라이언트가 서버에 보내는 요구 메시지를 완전히 처리 하지 못한 경우처럼 클라이언트 측에서 오류가 발생한 것을 의미
500번대 | 서버 측 에러 | 서버 자체에서 생긴 오류 상황이나 클라이언트의 요구 사항을 제대로 처리 할 수 없을 때 발생

- 200 OK: 클라이언트의 요청이 성공
- 201 Created : 클라이언트의 PUT 요청이 성공적이라는 것을 나타낸다.
- 301 Moved Permanently : 브라우저의 요청을 다른 URL로 항시 전달하는 것을 의미
- 302 Moved Temporarily : 브라우저의 요청을 임시 URL로 바꾸고 Location 헤더에 임시로 변경한 URL 정보를 적는다. (클라이언트가 같은 요청을 하면 기존 URL로 돌아간다)
- 304 Not Modified : 브라우저가 서버에 요청한 자료에 대해 서버는 클라이언트 내에 복사된 캐시를 사용하면 된다는 것을 의미
- 400 Bad Request: 클라이언트가 서버에 잘못된 요청을 했다는 것을 나타냄(URL 주소 중간에 빈공간을 넣는 등)
- 401 Unauthorized : 서버가 클라이언트의 요청에 대해 HTTP 인증 확인을 요구하는 것을 의미
- 403 Forbidden : 클라이언트의 요청에 대해 접근을 차단하는 것을 나타냄
- 404 Not Found : 클라이언트가 서버에 요청한 자료가 존재하지 않음을 나타낸다.
- 405 Method Not Allowed : 클라이언트가 요청에 이용한 메소드는 해당 URL에 지원이 불가능을 나타냄
- 413 Request Entity Too Large : 클라이언트가 요청한 보디가 서버에서 처리하기에는 너무 크다는 것을 나타냄
- 500 Internal Server Error : 서버가 클라이언트의 요청을 실행 할 수 없을 때 500상태 코드 



