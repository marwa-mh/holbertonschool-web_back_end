export default class Building {
    constructor(sqft) {
        
        this.validateAndAssignSqft(sqft);
        if (this.constructor !== Building && 
            this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage
        ) {
            throw new Error('Class extending Building must override evacuationWarningMessage');
        }
    }

    get sqft() {
        return this._sqft;
    }

    set sqft(sqft) {
        this.validateAndAssignSqft(sqft);
    }

    validateAndAssignSqft(sqft) {
      if (typeof sqft === 'number') {
      this._sqft = sqft;
    } else {
      throw new TypeError('sqft must be a number');
    }
    }

    evacuationWarningMessage() {
        throw new Error('Class extending Building must override evacuationWarningMessage');
    } 
}