export default function inputDataValueParser(currValue: string, proposedValue: string) {
  if (!/^[0-9.\n\s]*$/.test(proposedValue)) return currValue;
  return proposedValue.replace(/[ \t]+/g, '\n');
}
