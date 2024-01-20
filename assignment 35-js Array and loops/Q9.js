// Iterate through the array, ["HTML", "CSS", "JS", "React", "Redux", "Node",
// "Express", "MongoDB"] using a for loop or for of loop and print out the items.

const tech = [
  "HTML",
  "CSS",
  "JS",
  "React",
  "Redux",
  "Node",
  "Express",
  "MongoDB",
];

for (let i = 0; i < tech.length; i++) {
  console.log(tech[i]);
}

for (let i of tech) {
  console.log(i);
}
