// The following is an array of 10 students ages:
// const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
// Sort the array and find the min and max age
// Find the median age(one middle item or two middle items divided by two)
// Find the average age(all items divided by number of items)
// Find the range of the ages(max minus min)
// Compare the value of (min - average) and (max - average), use abs()
// method

const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24];
const shortedAges = ages.slice().sort((a, b) => a - b);
console.log("Shorted ages :");
console.log(shortedAges);

let minAge = shortedAges[0];
let maxAge = shortedAges[shortedAges.length - 1];
console.log(`minimum age is ${minAge}`);
console.log(`maximum age is ${maxAge}}`);

let medianAge;
if (shortedAges.length % 2 === 0) {
  medianAge =
    (shortedAges[shortedAges.length / 2 - 1] +
      shortedAges[shortedAges.length / 2]) /
    2;
} else {
  medianAge = shortedAges[Math.floor(shortedAges.length / 2)];
}

console.log(`Median age is ${medianAge}`);

let averageAge = Math.floor(
  ages.reduce((sum, age) => sum + age, 0) / ages.length
);
console.log(`Average of all ages ${averageAge}`);

let ageRange = maxAge - minAge;
console.log(`Age range is ${ageRange}`);

let minAverageDiff = Math.abs(minAge - averageAge);
let maxAverageDiff = Math.abs(maxAge - averageAge);

console.log(`|Min - Average|: ${minAverageDiff}`);
console.log(`|Max - Average|: ${maxAverageDiff}`);
