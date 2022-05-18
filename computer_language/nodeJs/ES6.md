# ECMAScript 2015(ES6)

## 1. ES6 Syntax
- let, const의등장
- default parameters
```javascript
function say(message='Hi') {
    console.log(message);
}

say(); // 'Hi'
say('Hello') // 'Hello'

function put(toy, toyBox = []) {
    toyBox.push(toy);
    return toyBox;
}

console.log(put('Toy Car'));
// -> ['Toy Car']
console.log(put('Teddy Bear'));
// -> ['Teddy Bear'], not ['Toy Car','Teddy Bear']
```
- rest Parameters
    - ...args, ...rest, ...temp
```javascript
function fn(a,b,...args) {
   //...
}

fn(1, 2, 3, "A", "B", "C");
// The args array stores the following values:
// [3,'A','B','C']

```
- Spread Operator
```javascript
const odd = [1,3,5];
const combined = [...odd, 2,4,6];
console.log(combined);
-> [ 1, 3, 5, 2, 4, 6 ]

const odd = [1,3,5];
const combined = [2,...odd, 4,6];
console.log(combined);
-> [ 2, 1, 3, 5, 4, 6 ]
```
- for ..of
  - array.entries(): 파이썬의 enumerate와 비슷
```javascript
let scores = [80, 90, 70];

for (let score of scores) {
    score = score + 5;
    console.log(score);
}

-> 85
95
75


// enumerate, 인덱스, 값
let colors = ['Red', 'Green', 'Blue'];

for (const [index, color] of colors.entries()) {
    console.log(`${color} is at index ${index}`);
}


// 딕셔너리처럼 사용하기

const ratings = [
    {user: 'John',score: 3},
    {user: 'Jane',score: 4},
    {user: 'David',score: 5},
    {user: 'Peter',score: 2},
];

let sum = 0;
for (const {score} of ratings) {
    sum += score;
}

console.log(`Total scores: ${sum}`); // 14


// iterating over strings
let str = 'abc';
for (let c of str) {
    console.log(c);
}
-> a
b
c

```

- 템플릿 리터럴
  - Expression interpolation(표현식 삽입)
  
```javascript
let firstName = 'John',
let lastName = 'Doe';

let greeting = 'Hi ' + firstName + ', ' + lastName;
console.log(greeting); // Hi John, Doe

let greeting = `Hi ${firstName}, ${lastName}`;
console.log(greeting); // Hi John, Doe

```

- 객체 리터럴
  - 객체 초기화 단순화
  ```javascript
  // 기존 자바 스크립트
  function createMachine(name, status) {
      return {
          name: name,
          status: status
      };
  }
  
  // ES6 적용(value값 생략 가능; 자동 key,value 생성)
  function createMachine(name, status) {
      return {
          name,
          status
      };
  }
  ```
  - 프로퍼티 이름 자동 계산
  ```javascript
  let name = 'machine name';
  let machine = {
      [name]: 'server',
      'machine hours': 10000
  };
  
  console.log(machine[name]); // server
  console.log(machine['machine hours']); // 10000
  
  let prefix = 'machine';
  let machine = {
      [prefix + ' name']: 'server',
      [prefix + ' hours']: 10000
  };
  
  console.log(machine['machine name']); // server
  console.log(machine['machine hours']); // 10000
  ```
  - 간결한 메소드 구문
  ```javascript
  // 기존 javascript
  let server = {
      name: "Server",
      restart: function () {
          console.log("The" + this.name + " is restarting...");
      }
  };
  
  // ES6 문법 적용
  let server = {
      name: 'Server',
      restart() {
          console.log("The" + this.name + " is restarting...");
      }
  };
  ```

## 2. 배열, 객체 비구조화(Destructuring)
- 배열 비 구조화
  - 변수 교환(swap)
  ```javascript
  let a = 10, 
      b = 20;
  
  [a, b] = [b, a];
  
  console.log(a); // 20
  console.log(b); // 10
  ```
```javascript
function getScores() {
   return [70, 80, 90];
}

// 기존 javascript
let scores = getScores();

let x = scores[0], 
    y = scores[1], 
    z = scores[2];

// ES6 문법 적용
let [x, y, z] = getScores();

console.log(x); // 70
console.log(y); // 80
console.log(z); // 90

let a, b;
[a, b] = [10, 20];
console.log(a); // 10
console.log(b); // 20

// 중첩 배열 비구조화
function getProfile() {
    return [
        'John',
        'Doe',
        ['Red', 'Green', 'Blue']
    ];
}

let [
    firstName,
    lastName,
    [
        color1,
        color2,
        color3
    ]
] = getProfile();

console.log(color1, color2, color3); // Red Green Blue
```


- 객체 비 구조화
  ```javascript
  let person = {
      firstName: 'John',
      lastName: 'Doe'
  };
  
  let { firstName, lastName } = person;
  
  console.log(firstName); // 'John'
  console.log(lastName); // 'Doe'
  ```

## 3. 모듈
- ES6 모듈은 자동으로 Export 하지 않습니다. 반드시 export를 명시해주어야 사용이 가능합니다.
```javascript
// file1.js
export let message = 'ES6 Modules';

// file2.js
import { message } from './message.js'

const h1 = document.createElement('h1');
h1.textContent = message

document.body.appendChild(h1)
```
- ES6의 모듈 추가의 가장 큰 의의는 파일 단위가 아닌 객체, 함수 단위의 사용을 위함

## 4. 클래스
- 클래스는 object를 만들기 위한 청사진이다.
- 데이터화 함수를 캡슐화한다.

```javascript
// javascript, 클래스 개념이 없었음
function Person(name) {
    this.name = name;
}

Person.prototype.getName = function () {
    return this.name;
};

var john = new Person("John Doe");
console.log(john.getName());

// ES6
class Person {
    constructor(name) {
        this.name = name;
    }
    getName() {
        return this.name;
    }
}

// 선언 *new*
let john = new Person("John Doe");
// let john = Person("John Doe");
// Uncaught TypeError: Class constructor Person cannot be invoked without 'new'


// 사용
let name = john.getName();
console.log(name); // "John Doe"

console.log(typeof Person); // function
console.log(john instanceof Person); // true
console.log(john instanceof Object); // true
```

## 5. 화살표 함수
- 화살표 함수는 함수표현식에 비해 더 짧은 구문으로 작성하기 위해 고안되었음
- 선언 및 호출
```javascript
// 매개변수 지정 방법
    () => { ... } // 매개변수가 없을 경우
     x => { ... } // 매개변수가 한 개인 경우, 소괄호를 생략할 수 있다.
(x, y) => { ... } // 매개변수가 여러 개인 경우, 소괄호를 생략할 수 없다.

// 함수 몸체 지정 방법
x => { return x * x }  // single line block
x => x * x             // 함수 몸체가 한줄의 구문이라면 중괄호를 생략할 수 있으며 암묵적으로 return된다. 위 표현과 동일하다.
() => {           // multi line block.
  const x = 10;
  return x * x;
};

() => { return { a: 1 }; }
() => ({ a: 1 })  // 위 표현과 동일하다. 객체 반환시 소괄호를 사용한다.


```

```javascript
// 기존함수
let add = function (x, y) {
	return x + y;
};

console.log(add(10, 20)); // 30

// 화살표 함수
let add = (x, y) => x + y;

console.log(add(10, 20)); // 30;

// {}를 사용하고싶다면 return을 반드시 붙여줘야함.
let add = (x, y) => { return x + y; };


```

### 화살표 함수를 사용하면 안될때
- 객체 메소드
```javascript
// 화살표 함수
const counter = {
  count: 0,
  next: () => ++this.count,
  current: () => this.count
};

console.log(counter.next()); // NaN

// 객체 리터럴
const counter = {
    count: 0,
    next() {
        return ++this.count;
    },
    current() {
        return this.count;
    }
};

console.log(counter.next()); // 1
```
- Prototype methods
```javascript
// 화살표함수, 전ㄴ역 객체를 참조 하기때문에 사용금지
function Counter() {
    this.count = 0;
}

Counter.prototype.next = () => {
    return this.count;
};

Counter.prototype.current = () => {
    return ++this.next;
}

// Good
function Counter() {
    this.count = 0;
}

Counter.prototype.next = function () {
    return this.count;
};

Counter.prototype.current = function () {
    return ++this.next;
}
```
- arguments를 사용하는 객체
```javascript
// bad
const concat = (separator) => {
    let args = Array.prototype.slice.call(arguments, 1);
    return args.join(separator);
}

// good
function concat(separator) {
    let args = Array.prototype.slice.call(arguments, 1);
    return args.join(separator);
}
```
- 이벤트 핸들러
```javascript
// bad
username.addEventListener('keyup', () => {
  greeting.textContent = 'Hello ' + this.value;
});
-> Hello undefined

// Good
username.addEventListener('keyup', function () {
    input.textContent = 'Hello ' + this.value;
});
```

## 6. 프로미스
- 프로미스란, 비동기 처리를 위한 패턴
  - 자바스크립트는 비동기 처리를 위한 하나의 패턴으로 콜백 함수를 사용한다. 하지만 전통적인 콜백 패턴은 콜백 헬로 인해 가독성이 나쁘고 비동기 처리중 발생하는 에러 처리가 곤란하며 여러개의 비동기 처리를 한번에 처리하는 것에도 한계가 있다.
  
- 콜백 헬
  - 