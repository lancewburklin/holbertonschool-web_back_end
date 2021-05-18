/* eslint no-param-reassign: "error" */
export default function updateStudentGradeByCity(students, city, newGrades) {
  const result = students.filter((student) => student.location === city);
  function mapping(student) {
    let thing = 'N/A';
    for (let i = 0; i < newGrades.length; i += 1) {
      if (newGrades[i].studentId === student.id) {
        thing = newGrades[i].grade;
      }
    }
    student.grade = thing;
  }
  result.map((x) => mapping(x));
  return students;
}
