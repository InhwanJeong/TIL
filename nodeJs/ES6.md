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
```javascript


```