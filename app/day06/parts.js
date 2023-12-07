const { readFile, strToInt } = require("../support/utils");

const parse_line_to_num = (line, clear_str) =>
  line
    .replace(clear_str, "")
    .split(" ")
    .filter((n) => n)
    .map((n) => strToInt(n));

const parser_part_1 = (lines) => {
  const [time, distance] = lines;
  const t = parse_line_to_num(time, "Time: ");
  const d = parse_line_to_num(distance, "Distance: ");
  return t.map((t, i) => [t, d[i]]);
};

const main = () => {
  const lines = readFile("day06/input.txt").split("\n");

  const races = parser_part_1(lines);
  const results = races.map(([t, d]) => {
    return Array.from(Array(t).keys()).reduce((acc, c) => {
      if ((t - c) * c > d) return acc + 1;
      return acc;
    }, 0);
  });
  return results.reduce((a, b) => a * b, 1);
};

console.info(main());
