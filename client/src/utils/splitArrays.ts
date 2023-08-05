export default function splitArrays<T>(
  array1: T[],
  array2: T[],
): Array<Array<T>> {
  if (array1.length !== array2.length)
    throw new Error('Arrays must be of the same length');

  return array1.map((value, index) => [value, array2[index]]);
}
