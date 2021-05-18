export default function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  const view = new DataView(buff);
  if (position > length) {
    throw Error('Position outside range');
  }
  view.setInt8(position, value);
  return view;
}
