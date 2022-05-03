# 기초

### print문, 주석
```javascript
// 한줄 주석
/* 여러줄 주석*/
console.log("hello");
```

### 변수, 상수
- 기본적인 사용법
```javascript
/* var는 사용을 삼가는게 좋다. 
    ex1)
        console.log(temp);
        var temp;
    ex2)
        for(var i=0; i<5; i++){
            console.log(i)
        }  
        console.log(i)
*/

// 상수
const MAX = 10 ;
// 변수
let message = 'hello world';

console.log(message);
```
- Undefined vs. undeclared variables
```javascript
let message;
console.log(message); // undefined

console.log(counter);
            ^
ReferenceError: counter is not defined
```

### 데이터 타입
- primitive
    - null
    - undefined
    - boolean
    - number
    - string
    - symbol – available from ES2015
    - bigint – available from ES2020
    
- complex
    - object(배열, 객체, 함수)
    
- 자바스크립트는 동적 타입 언어이다.
    - 타입 확인 typeof()
```javascript
let counter = 120; // counter is a number
counter = false;   // counter is now a boolean
counter = "foo";   // counter is now a string

let counter = 120;
console.log(typeof(counter)); // "number"

counter = false; 
console.log(typeof(counter)); // "boolean"

counter = "Hi";
console.log(typeof(counter)); // "string"

// NaN
console.log('a'/2); // NaN;
console.log(NaN/2); // NaN
console.log(NaN == NaN); // false

// 비교 연산자
let compare = 2 > 50; // false

// 논리 연산자
let logic = (7 > 2) && (3 < 9);  // true
```

## 함수, if문, for문
```javascript
// 함수
function myFunction(x, y) {
  return x + y;
}

// if 문
if (time < 10) {
  greeting = 'Good morning';
} else if (time < 20) {
  greeting = 'Good day';
} else {
  greeting = 'Good evening';
}

// for 문
for (var i = 0; i < 10; i++) {
  // do something
}
```

## 객체(object)
- 자바스크립트는 객체(object) 기반의 스크립트 언어이며 자바스크립트를 이루고 있는 거의 “모든 것”이 객체이다. 
  - 원시 타입(Primitives)을 제외한 나머지 값들(함수, 배열, 정규표현식 등)은 모두 객체이다.
  
```javascript
var person = {
  name: 'Jeong',
  gender: 'male',
  sayHello: function () {
    console.log('I'm ' + this.name);
  }
};

console.log(typeof person); // object
console.log(person); // { name: 'Jeong', gender: 'male', sayHello: [Function: sayHello] }

person.sayHello(); // I'm Jeong
```

## 연산자
- 동등, 일치 비교 연산자
```javascript
// 동등 비교
1 == 1    // true
// 타입은 다르지만 암묵적 타입 변환을 통해 타입을 일치시키면 같은 값을 가진다.
1 == '1'   //true
1 == 2    // false

// 일치 비교
1 === 1   // true
1 === '1' // false
```

- 삼항 조건 연산자
  
```javascript
//조건식 ? 조건식이 ture일때 반환 : 조건식이 false일때 반환
let x = 2;

let result = x % 2 ? '홀수' : '짝수';

console.log(result); // 짝수
```
  
