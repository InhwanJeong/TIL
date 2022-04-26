# node.js

- javascript 언어 기반의
- 웹서버
- 웹 브라우저에서만 사용할 수 있는 자바스크립트 함수가 다수 존재
    - alert()
- express: nodejs 프레임워크
    - 최소화: 최소한의 프레임워크만 제공
    - 유연함: 클라이언트의 HTTP 요청을 받고, HTTP 응답을 반환
    - 속도
- ES(ECMAScript)6
    - 자바스크립트를 표준화 하기위해 만들어진 ECMA-262 기술 규격에 따라 정의하고 있는 표준화 된 스크립트 언어
    - 변경점
        - const, let: const는 상수 let은 변수, 기존은 var만 사용
        - default parameter: 기존에는 디폴트 매개변수를 넣을 수 없었는데 ES6부터 가능하게 변경되음
        - for..of: 파이썬의 for..in과 동일
            - 

- TypeScript
- 이벤트 주도 프로그래밍(event-driven programming): 어떤 이벤트가 일어날지, 그 이벤트에 어떻게 반응해야할 지 프로그래머가 이해해야한다는 의미.

## 1. npm
- npm(node package manager): 설치, 삭제, 업그레이드, 의존성 관리 등
- 대부분의 노드 패키지는 MIT 라이선스지만, 그렇지 않은 패키지들도 존재하니 주의가 필요함.
- npm 설치
```
npm install {package} -g // 전역으로 설치
npm install {package} // 프로젝트에 설치
```

## 2. Express
- express 설치
```bash
npm install express@4 -g
npm install test
```
### (1) 스캐폴딩(scaffolding; 비계, 발판)
- 대부분의 프로젝트는 뼈대가 되는 보일러플레이트가 필요한데, 프로젝트를 시작할 때마다 코드를 반복적으로 생산하지 않아도 되는 아이디어
- 루비에서 도입한 개념
- 템플릿 엔진
    - dust|ejs|hbs|hjs|jade|pug|twig|vash
- express-generator
```bash
npm install express-generator -g
express --view=pug myapp
cd myapp
npm install
```
