const fs = require("node:fs");
const path = require("node:path");

const getProjectRoot = () => path.resolve(__dirname, "../");

const readFile = (filename) => {
  const absolutePath = path.join(getProjectRoot(), filename);
  console.info(`Reading file: ${absolutePath}`);
  try {
    return fs.readFileSync(absolutePath, "utf8");
  } catch (err) {
    console.error(err);
  }
};

module.exports = readFile;
