export default function removeWhitespaces(inputString: string) {
  // Create a regular expression to match whitespace characters (spaces, tabs, and new lines)
  const pattern = /[ \t]+/g;

  // Use the replace method to remove all occurrences of whitespace characters
  const resultString = inputString.replace(pattern, '');

  return resultString;
}
