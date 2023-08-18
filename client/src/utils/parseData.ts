import removeWhitespaces from './removeWhitespaces';
import { parseRow } from './rowParsers';

function parseData(xvalue: string, yvalue: string) {
  const xrows = removeWhitespaces(xvalue).split('\n');
  const yrows = removeWhitespaces(yvalue).split('\n');
  const xlen = xrows.length;
  const ylen = yrows.length;
  let data: [number[], number[]] = [[], []];
  for (let i = 0; i < Math.min(xlen, ylen); i++) {
    const xrow = xrows[i];
    const yrow = yrows[i];
    if (xrow && yrow && !isNaN(parseFloat(xrow)) && !isNaN(parseFloat(yrow))) {
      data[0].push(parseRow(xrow));
      data[1].push(parseRow(yrow));
    }
  }
  return data;
}
export default parseData;
