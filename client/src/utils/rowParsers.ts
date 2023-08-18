function parseRow(row: string): number {
  const number = parseFloat(row);
  return number;
}
function parseRowBackwards(numbers: number[]): string {
  const result = numbers.map((number) => `${number}`).join('\n');
  return result;
}
export { parseRow, parseRowBackwards };
