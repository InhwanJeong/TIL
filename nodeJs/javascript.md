## 기초

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
    - object
    
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
```