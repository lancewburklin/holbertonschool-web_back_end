export default function hasValuesFromArray(theSet, theArray) {
  for (let i = 0; i < theArray.length; i += 1) {
    if (theSet.has(theArray[i]) === false) {
      return false;
    }
  }
  return true;
}
