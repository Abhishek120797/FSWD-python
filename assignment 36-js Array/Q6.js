// Declare a function name capitalizeArray. It takes array as a parameter and it returns
// the - capitalizedarray.

function capitalizeArray(inputArray) {
  if (!Array.isArray(inputArray)) {
    throw new Error("Input must be an array");
  }

  const capitalazedArray = [];

  for (let i = 0; i < inputArray.length; i++) {
    if (typeof inputArray[i] == "string") {
      const capitalString = inputArray[i].toUpperCase();
      capitalazedArray.push(capitalString);
    } else {
      capitalazedArray.push(inputArray[i]);
    }
  }
  return capitalazedArray;
}

const input = ["apple", "banana", "cherry", 10, true];
const result = capitalizeArray(input);
console.log(result);
