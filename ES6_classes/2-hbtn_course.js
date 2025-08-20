export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('TypeError: Name must be a string');
    }
    this.validateLength(length);
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('TypeError: Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    this.validateLength(length);
    this._length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    this._students = students;
  }

  validateLength(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new Error('TypeError: Length must be a number');
    }
  }
}
