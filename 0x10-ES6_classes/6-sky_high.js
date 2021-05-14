import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  set floors(Numfloors) {
    if (typeof (Numfloors) !== 'number') {
      throw TypeError('Floors must be a number');
    }
    this._floors = Numfloors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
