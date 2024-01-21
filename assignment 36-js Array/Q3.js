// Develop a small script which generate any number of characters random id.
// Example:
// fe3jo1gl124g
// xkqci4utda1lmbelpkm03rba

const characters =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789";

function idGenerater(idLength) {
  let id = "";
  for (let i = 0; i < idLength; i++) {
    id += characters[Math.floor(Math.random() * characters.length)];
  }
  return id;
}

console.log(idGenerater(5));
