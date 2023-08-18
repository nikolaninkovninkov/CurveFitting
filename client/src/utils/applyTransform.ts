import removeWhitespaces from './removeWhitespaces';
import { parseRowBackwards } from './rowParsers';

type FunctionalTransform = 'reciprocal' | 'log' | 'log10' | 'exp' | 'square' | 'sqrt';
function applyFunctionalTransform(values: string, transform: FunctionalTransform) {
  const numbers = values
    .trim()
    .split('\n')
    .map((row) => parseFloat(row));
  switch (transform) {
    case 'reciprocal':
      return parseRowBackwards(numbers.map((n) => 1 / n));
    case 'log':
      return parseRowBackwards(numbers.map(Math.log));
    case 'log10':
      return parseRowBackwards(numbers.map(Math.log10));
    case 'exp':
      return parseRowBackwards(numbers.map(Math.exp));
    case 'square':
      return parseRowBackwards(numbers.map((n) => Math.pow(n, 2)));
    case 'sqrt':
      return parseRowBackwards(numbers.map(Math.sqrt));
  }
}
type AxisTransform = 'times_other_axis' | 'divided_by_other_axis';
function applyAxisTransform(primary_values: string, other_values: string, transform: AxisTransform) {
  const [primary_nums, other_nums] = [primary_values, other_values].map((values) =>
    values
      .trim()
      .split('\n')
      .map((row) => parseFloat(row)),
  );
  console.log(primary_nums, other_nums);
  if (primary_nums.length !== other_nums.length)
    throw new Error('Primary value array and other array must be of the same length');

  switch (transform) {
    case 'times_other_axis':
      return parseRowBackwards(primary_nums.map((p, i) => p * other_nums[i]));
    case 'divided_by_other_axis':
      return parseRowBackwards(primary_nums.map((p, i) => p / other_nums[i]));
  }
}
export { applyFunctionalTransform, applyAxisTransform };
