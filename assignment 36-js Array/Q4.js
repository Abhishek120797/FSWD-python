// Create a countries array, check if there is a country or countries containing the word
// 'and'. If there are countries containing 'and', print it as array. If there is no country
// containing the word 'and', print 'All these countries are without and'.

const countries = [
  "United States",
  "Canada",
  "United Kingdom",
  "Germany",
  "France",
  "Japan",
  "China",
  "India",
  "Brazil",
  "Australia",
  "South Africa",
  "Mexico",
  "Italy",
  "Spain",
  "Russia",
  "South Korea",
  "Argentina",
  "Turkey",
  "Egypt",
  "Nigeria",
  "England",
  "Ireland",
];

let andContains = countries.filter((item) => {
  if (item.includes("and")) {
    return item;
  }
});

if (andContains.length == 0) {
  console.log(countries);
} else {
  console.log(andContains);
}
