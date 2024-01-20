// Write a code which can give grades to students according to theirs scores:
// a. 80-100, A
// b. 70-89, B
// c. 60-69, C
// d. 50-59, D
// e. 0-49, F

let score = 27;
if (score >= 90 && score <= 100) {
  console.log("A");
}
if (score >= 70 && score <= 89) {
  console.log("B");
}
if (score >= 60 && score <= 69) {
  console.log("C");
}
if (score >= 50 && score <= 59) {
  console.log("D");
}
if (score >= 0 && score <= 49) {
  console.log("F");
}
