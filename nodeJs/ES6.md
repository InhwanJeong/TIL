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