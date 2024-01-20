// Write a script which generates a random hexadecimal number.

function generateRandomHexNumber(length) {
  const characters = "0123456789ABCDEF";
  let randomHex = "0x"; // Ensuring the number starts with '0x'

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    randomHex += characters.charAt(randomIndex);
  }

  return randomHex;
}

const randomHexNumber = generateRandomHexNumber(6);
console.log(randomHexNumber);
