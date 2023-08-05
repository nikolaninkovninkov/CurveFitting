export default interface CurveFitResponseData {
  r_squared: number;
  output_function: string;
  [key: string]: { value: number; var: number } | number | string;
}
