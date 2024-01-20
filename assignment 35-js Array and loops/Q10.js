// Create a human readable time format using the Date time object
// a. YYYY-MM-DD HH:mm
// b. DD-MM-YYYY HH:mm
// c. DD/MM/YYYY HH:mm

const newDate = new Date();
const year = newDate.getFullYear();
const month = String(newDate.getMonth() + 1).padStart(2, "0");
const day = String(newDate.getDate()).padStart(2, "0");
const hour = String(newDate.getHours()).padStart(2, "0");
const minute = String(newDate.getMinutes()).padStart(2, "0");
console.log(`${year}-${month}-${day} ${hour}:${minute}`);
console.log(`${day}-${month}-${year} ${hour}:${minute}`);
console.log(`${year}/${month}/${day} ${hour}:${minute}`);
