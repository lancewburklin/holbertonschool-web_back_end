export default function getListStudentIds(people) {
  if (Array.isArray(people) === false) {
    return [];
  }
  const allIDs = people.map((element) => element.id);
  return allIDs;
}
