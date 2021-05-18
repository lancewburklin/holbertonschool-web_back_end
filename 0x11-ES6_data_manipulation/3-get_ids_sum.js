export default function getStudentIdsSum(students) {
  const reducer = (accumulator, item) => accumulator + item.id;
  return students.reduce(reducer, 0);
}
