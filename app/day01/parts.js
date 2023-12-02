const { readFile, strToInt } = require("../support/utils");

const NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];

const main = () => {
  return readFile("day01/input.txt")
    .split("\n")
    .map((line) => line.split("").filter((char) => NUMBERS.includes(char)))
    .map((nums) => strToInt(`${nums[0]}${nums[nums.length - 1]}`))
    .reduce((acc, cur) => acc + cur, 0);
};

console.info(main());
