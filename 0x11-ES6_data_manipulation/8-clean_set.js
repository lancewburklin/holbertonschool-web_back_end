export default function cleanSet(set, startString) {
  let newStr = '';
  if (startString === '') {
    return newStr;
  }
  set.forEach((x) => {
    const strSub = x.substr(0, startString.length);
    if (strSub === startString) {
      newStr += x.substr(startString.length, x.length - 1);
      newStr += '-';
    }
  });
  return newStr.slice(0, -1);
}
