// 1. In the following shopping cart add, remove, edit itemsconst shoppingCart = ['Milk',
// 'Coffee', 'Tea', 'Honey']
// a. add 'Meat' in the beginning of your shopping cart if it has not been already
// added
// b. add Sugar at the end of you shopping cart if it has not been already added
// c. remove 'Honey' if you are allergic to honey
// d. modify Tea to 'Green Tea'

const shoppingCart = ["Milk", "Coffee", "Tea", "Honey"];

if (!shoppingCart.includes("Meat")) {
  shoppingCart.unshift("Meat");
}
console.log(shoppingCart);

if (!shoppingCart.includes("Suguar")) {
  shoppingCart.push("Sugar");
}
console.log(shoppingCart);

let allergeticToHoney = true;

if (allergeticToHoney) {
  const honeyIndex = shoppingCart.indexOf("Honey");
  if (honeyIndex !== -1) {
    shoppingCart.splice(honeyIndex, 1);
  }
}
console.log(shoppingCart);

const teaIndex = shoppingCart.indexOf("Tea");

if (teaIndex !== -1) {
  shoppingCart[teaIndex] = "Green Tea";
}
console.log(shoppingCart);
