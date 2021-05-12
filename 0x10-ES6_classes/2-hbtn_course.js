export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(newName) {
    if (typeof (newName) === 'string') {
      this._name = newName;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get name() {
    return this._name;
  }

  set length(newLength) {
    if (typeof (newLength) === 'number') {
      this._length = newLength;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  get length() {
    return this._length;
  }

  set students(newStudents) {
    if (typeof newStudents === 'object') {
      this._students = newStudents;
    } else {
      throw TypeError('Students must be an array');
    }
  }

  get students() {
    return this._students;
  }
}
