// Write a function called sumOfArrayItems, it takes an array parameter and return the
// sum of all the items. Check if all the array items are number types. If not give return
// reasonable feedback.

function sumOfArrayItems(numArray) {
  if (!Array.isArray(numArray)) {
    return new Error("Input must be an array");
  }

  if (numArray.every((item) => typeof item == "number")) {
    let sum = 0;
    for (let i = 0; i < numArray.length; i++) {
      sum += numArray[i];
    }
    return sum;
  } else {
    console.log(
      `In Array some element might be not number so we do not add them`
    );
  }
}

const str = "1,2,3,4,5,6,7,8,9,10";
const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numStr = [1, 2, 3, 4, "5", 6, 7, "8", 9, 10];

console.log(sumOfArrayItems(num));
console.log(sumOfArrayItems(numStr));
console.log(sumOfArrayItems(str));
