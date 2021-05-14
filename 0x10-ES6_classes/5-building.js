export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  set sqft(newSqft) {
    if (typeof (newSqft) === 'number') {
      this._sqft = newSqft;
    }
  }

  get sqft() {
    return this._sqft;
  }
}
