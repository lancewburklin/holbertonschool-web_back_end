export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const ret = [...set].filter((x) => {
    if (x.substr(0, startString.length) === startString) {
      return (x.substr(startString.length, x.length));
    }
    return '';
  });
  function reducer(accumulator, currentValue) {
    let subAcc = '';
    if (accumulator !== '') {
      subAcc += '-';
    }
    subAcc += currentValue.substr(startString.length, currentValue.length);
    return accumulator + subAcc;
  }
  const res = ret.reduce(reducer, '');
  return res;
}
