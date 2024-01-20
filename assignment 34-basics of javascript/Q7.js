// Create a human readable time format using the Date time object
// a. YYYY-MM-DD HH:mm
// b. DD-MM-YYYY HH:mm
// c. DD/MM/YYYY HH:mm

const date = new Date();
//YYYY-MM-DD HH:mm
console.log(
  date.getFullYear(),
  "-",
  date.getMonth(),
  "-",
  date.getDate(),
  " ",
  date.getHours(),
  ":",
  date.getMinutes()
);
//DD-MM-YYYY HH:MM
console.log(
  date.getDate(),
  "-",
  date.getMonth(),
  "-",
  date.getFullYear(),
  " ",
  date.getHours(),
  ":",
  date.getMinutes()
);
//DD/MM/YYYY HH:mm
console.log(
  date.getDate(),
  "/",
  date.getMonth(),
  "/",
  date.getFullYear(),
  " ",
  date.getHours(),
  ":",
  date.getMinutes()
);

// console.log(date.toISOString());
// console.log(date.toJSON());
// console.log(date.toLocaleString());
// console.log(date.toLocaleDateString());
// console.log(date.toLocaleTimeString());
console.log(new Date());
