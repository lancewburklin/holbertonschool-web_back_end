export default function updateUniqueItems(newMap) {
  if ((newMap instanceof Map) === false) {
    throw Error('Cannot process');
  }
  const mapCopy = new Map(newMap.entries());
  function updateCopy(value, key) {
    if (value === 1) {
      newMap.set(key, 100);
    }
  }
  mapCopy.forEach(updateCopy);
}
