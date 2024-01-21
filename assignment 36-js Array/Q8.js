// Write a function called modifyArray takes array as parameter and modifies the fifth
// item of the array and return the array. If the array length is less than five it return 'item
// not found'

function modifyArray(array) {
  if (!Array.isArray(array)) {
    throw new Error("Input must be an array");
  }
  if (array.length < 5) {
    console.log("Item not found");
  } else {
    array[4] = 0;
  }
}

const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
modifyArray(num);
console.log(num);
