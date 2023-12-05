const { readFile, strToInt } = require("../support/utils");

const createArrOfNums = (numbers) =>
  numbers
    .split(" ")
    .filter((i) => i)
    .map((i) => Number(i));

const parseNumbers = (numbers) => {
  const [wn, mn] = numbers.split("|");
  return [new Set(createArrOfNums(wn)), new Set(createArrOfNums(mn))];
};

const main = () => {
  let lines = readFile("day04/input.txt").split("\n");
  // This looks little hacky, because the input.txt has 1 extra empty line at the end
  lines = lines.slice(0, lines.length - 1);
  const games = lines.reduce((acc, line) => {
    const sline = line.split(":");
    return {
      ...acc,
      ...{
        [Number(sline[0].replace("Card", "").trim())]: parseNumbers(sline[1]),
      },
    };
  }, {});

  const matches = Object.values(games).map(([wm, my], index) =>
    Array.from(new Set([...wm].filter((x) => my.has(x))))
  );

  const total = Object.keys(games)
    .map((key, index) => {
      const nums = matches[index];
      return nums.length > 0
        ? nums.slice(0, nums.length - 1).reduce((acc, cur) => acc * 2, 1)
        : 0;
    })
    .reduce((acc, cur) => acc + cur, 0);
  return total;
};

console.assert(main() == 17803);
