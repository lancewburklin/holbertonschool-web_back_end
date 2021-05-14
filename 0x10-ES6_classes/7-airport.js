export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  set name(newName) {
    if (typeof (newName) !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = newName;
  }

  get name() {
    return this.name;
  }

  set code(newCode) {
    if (typeof (newCode) !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  get code() {
    return this._code;
  }

  toString() {
    return `[object ${this.code}]`;
  }
}
