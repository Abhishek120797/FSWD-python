// Write a function which checks if all the items of the array are the same data type.

function checkArrayItemType(array) {
  if (!Array.isArray(array)) {
    throw new Error("Input must be array");
  }
  if (array.length == 0) {
    return true;
  }
  const dataType = typeof array[0];
  return array.every((item) => typeof item == dataType);
}

const num = [1, 2, 3, 4, 5, 6];

console.log(checkArrayItemType(num));
