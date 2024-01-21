// Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all
// odds. Print sum of evens and sum of odds as array

let sumOfAllEven = 0;
let sumOfAllOdd = 0;

for (let i = 0; i <= 100; i++) {
  if (i % 2 == 0) {
    sumOfAllEven += i;
  } else {
    sumOfAllOdd += i;
  }
}

console.log(`sum of all even numbers from 0 to 100 is : ${sumOfAllEven}`);
console.log(`sum of all odd numbers from 0 to 100 is : ${sumOfAllOdd}`);
