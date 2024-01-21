// This is a fruit array , ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop
// without using a reverse method.
const fruits = ["banana", "orange", "mango", "lemon"];

console.log(fruits);

for (let i = 0; i < fruits.length / 2; i++) {
  let temp = fruits[i];
  fruits[i] = fruits[fruits.length - 1 - i];
  fruits[fruits.length - 1 - i] = temp;
}
console.log("After Reversing Array");

console.log(fruits);
