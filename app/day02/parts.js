const { readFile, strToInt } = require("../support/utils");

const REGEXES = {
  red: /\d+ red/g,
  green: /\d+ green/g,
  blue: /\d+ blue/g,
};

const CHECK_FOR_GAMES_WITH = {
  red: 12,
  green: 13,
  blue: 14,
};

const main = () => {
  const lines = readFile("day02/input.txt").split("\n");
  return lines.map((line) => {
    const [game, bags] = line.split(":");
    const [_, game_n] = game.split(" ");
    for (const regex in REGEXES) {
      if (
        bags?.match(REGEXES[regex])?.find((item) => {
          const [v, _] = item.split(" ");
          return strToInt(v) > CHECK_FOR_GAMES_WITH[regex];
        })
      ) {
        return 0;
      }
    }
    return strToInt(game_n);
  });
  //.reduce((acc, curr) => acc + curr, 0);
};

console.info(main());
