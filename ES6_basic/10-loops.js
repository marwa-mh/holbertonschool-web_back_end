/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
  for (const [key, value] of array.entries()) {
    array[key] = appendString + value;
  }
  return array;
}
