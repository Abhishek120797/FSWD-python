// This is a fruit array , ['banana', 'orange', 'mango', 'lemon'] reverse the order using
// loop without using a reverse method.

const fruit = ["banana", "orange", "mango", "lemon"];

for (let i = 0; i < fruit.length / 2; i++) {
  let temp = fruit[fruit.length - i - 1];
  fruit[fruit.length - i - 1] = fruit[i];
  fruit[i] = temp;
}

console.log(fruit);
